from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, aliased
from sqlalchemy import func, extract, or_, outerjoin
from database import get_db
from models import Transaction, Category, User
from routers.users import get_current_user

router = APIRouter(prefix="/api/orcamento", tags=["Orcamento"])


@router.get("/{ano}/{mes}")
def get_orcamento(
    ano: int,
    mes: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if mes < 1 or mes > 12:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mes invalido")

    rows = (
        db.query(
            Category.id,
            Category.nome,
            Category.limite_orcamento,
            func.coalesce(func.sum(Transaction.valor), 0).label("total_gasto"),
        )
        .outerjoin(
            Transaction,
            (Transaction.categoria_id == Category.id)
            & (Transaction.tipo == "despesa")
            & (extract("year", Transaction.data) == ano)
            & (extract("month", Transaction.data) == mes)
            & or_(
                Transaction.usuario_id == current_user.id,
                Transaction.compartilhada == True,
            ),
        )
        .filter(Category.tipo == "despesa")
        .group_by(Category.id, Category.nome, Category.limite_orcamento)
        .all()
    )

    resultado = []
    for cat_id, nome, limite, total in rows:
        limite_val = limite or 0
        resultado.append({
            "categoria": nome,
            "categoria_id": cat_id,
            "total_gasto": round(total, 2),
            "limite": limite_val,
            "saldo_restante": round(limite_val - total, 2),
        })

    return resultado
