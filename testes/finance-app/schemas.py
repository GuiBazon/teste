from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum


class TransactionTypeEnum(str, Enum):
    receita = "receita"
    despesa = "despesa"


class AccountTypeEnum(str, Enum):
    conta_corrente = "conta_corrente"
    cartao_credito = "cartao_credito"
    dinheiro = "dinheiro"


class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    token_convite: str


class UserUpdate(BaseModel):
    nome: str
    email: EmailStr
    senha: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    senha: str


class AccountCreate(BaseModel):
    nome: str
    tipo: AccountTypeEnum
    saldo_inicial: float = 0.0


class AccountResponse(BaseModel):
    id: int
    nome: str
    tipo: str
    saldo_inicial: float
    usuario_id: int

    class Config:
        from_attributes = True


class CategoryCreate(BaseModel):
    nome: str
    tipo: TransactionTypeEnum
    limite_orcamento: Optional[float] = None


class CategoryResponse(BaseModel):
    id: int
    nome: str
    tipo: str
    limite_orcamento: Optional[float]

    class Config:
        from_attributes = True


class TransactionCreate(BaseModel):
    descricao: str
    valor: float
    tipo: TransactionTypeEnum
    data: Optional[datetime] = None
    conta_id: int
    categoria_id: int
    compartilhada: bool = False
    parcelado: bool = False
    numero_parcelas: Optional[int] = None
    parcela_atual: Optional[int] = None


class TransactionResponse(BaseModel):
    id: int
    descricao: str
    valor: float
    tipo: str
    data: datetime
    usuario_id: int
    conta_id: int
    categoria_id: int
    compartilhada: bool
    parcelado: bool
    numero_parcelas: Optional[int]
    parcela_atual: Optional[int]

    class Config:
        from_attributes = True
