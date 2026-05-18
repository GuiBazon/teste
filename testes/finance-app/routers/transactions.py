from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from database import get_db
from models import Transaction, User
from schemas import TransactionCreate, TransactionResponse
from routers.users import get_current_user
from datetime import datetime
import calendar

router = APIRouter(prefix="/api/transactions", tags=["Transacoes"])


def _add_months(source: datetime, months: int) -> datetime:
    month = source.month - 1 + months
    year = source.year + month // 12
    month = month % 12 + 1
    day = min(source.day, calendar.monthrange(year, month)[1])
    return source.replace(year=year, month=month, day=day)


@router.post("/", response_model=list[TransactionResponse], status_code=status.HTTP_201_CREATED)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if transaction.parcelado:
        if not transaction.numero_parcelas or transaction.numero_parcelas < 2:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Transacao parcelada deve ter pelo menos 2 parcelas")
        if transaction.valor <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Valor deve ser positivo")
        valor_parcela = round(transaction.valor / transaction.numero_parcelas, 2)
        data_base = transaction.data or datetime.utcnow()
        transactions = []
        for i in range(1, transaction.numero_parcelas + 1):
            db_transaction = Transaction(
                descricao=f"{transaction.descricao} ({i}/{transaction.numero_parcelas})",
                valor=valor_parcela,
                tipo=transaction.tipo,
                data=_add_months(data_base, i - 1),
                usuario_id=current_user.id,
                conta_id=transaction.conta_id,
                categoria_id=transaction.categoria_id,
                compartilhada=transaction.compartilhada,
                parcelado=True,
                numero_parcelas=transaction.numero_parcelas,
                parcela_atual=i,
            )
            db.add(db_transaction)
            transactions.append(db_transaction)
        db.commit()
        for t in transactions:
            db.refresh(t)
        return transactions

    db_transaction = Transaction(
        descricao=transaction.descricao,
        valor=transaction.valor,
        tipo=transaction.tipo,
        data=transaction.data or datetime.utcnow(),
        usuario_id=current_user.id,
        conta_id=transaction.conta_id,
        categoria_id=transaction.categoria_id,
        compartilhada=transaction.compartilhada,
        parcelado=False,
        numero_parcelas=None,
        parcela_atual=None,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return [db_transaction]


@router.get("/", response_model=list[TransactionResponse])
def list_transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    transactions = db.query(Transaction).filter(
        or_(
            Transaction.usuario_id == current_user.id,
            Transaction.compartilhada == True
        )
    ).all()
    return transactions


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        or_(
            Transaction.usuario_id == current_user.id,
            Transaction.compartilhada == True
        )
    ).first()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transacao nao encontrada")
    return transaction


@router.put("/{transaction_id}", response_model=TransactionResponse)
def update_transaction(transaction_id: int, transaction: TransactionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.usuario_id == current_user.id
    ).first()
    if not db_transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transacao nao encontrada ou sem permissao")
    db_transaction.descricao = transaction.descricao
    db_transaction.valor = transaction.valor
    db_transaction.tipo = transaction.tipo
    db_transaction.data = transaction.data or datetime.utcnow()
    db_transaction.conta_id = transaction.conta_id
    db_transaction.categoria_id = transaction.categoria_id
    db_transaction.compartilhada = transaction.compartilhada
    db_transaction.parcelado = transaction.parcelado
    db_transaction.numero_parcelas = transaction.numero_parcelas
    db_transaction.parcela_atual = transaction.parcela_atual
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_transaction(transaction_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.usuario_id == current_user.id
    ).first()
    if not db_transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transacao nao encontrada ou sem permissao")
    db.delete(db_transaction)
    db.commit()
