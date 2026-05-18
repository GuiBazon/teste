from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import extract, or_
from database import get_db
from models import Transaction, User
from routers.users import get_current_user
import csv
import io

router = APIRouter(prefix="/api/exportar", tags=["Exportacao"])


@router.get("/{usuario_id}/{ano}/{mes}")
def exportar_csv(
    usuario_id: int,
    ano: int,
    mes: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != usuario_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Voce so pode exportar seus proprios dados",
        )
    if mes < 1 or mes > 12:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mes invalido")

    transacoes = (
        db.query(Transaction)
        .filter(
            extract("year", Transaction.data) == ano,
            extract("month", Transaction.data) == mes,
            or_(
                Transaction.usuario_id == usuario_id,
                Transaction.compartilhada == True,
            ),
        )
        .order_by(Transaction.data)
        .all()
    )

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "id", "descricao", "valor", "tipo", "data",
        "usuario_id", "conta_id", "categoria_id",
        "compartilhada", "parcelado", "numero_parcelas", "parcela_atual",
    ])

    for t in transacoes:
        writer.writerow([
            t.id,
            t.descricao,
            t.valor,
            t.tipo,
            t.data.strftime("%Y-%m-%d %H:%M:%S") if t.data else "",
            t.usuario_id,
            t.conta_id,
            t.categoria_id,
            t.compartilhada,
            t.parcelado,
            t.numero_parcelas,
            t.parcela_atual,
        ])

    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=transacoes_{ano}_{mes}.csv"
        },
    )
