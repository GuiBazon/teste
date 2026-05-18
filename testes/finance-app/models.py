from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum
from datetime import datetime


class TransactionType(str, enum.Enum):
    RECEITA = "receita"
    DESPESA = "despesa"


class AccountType(str, enum.Enum):
    CONTA_CORRENTE = "conta_corrente"
    CARTAO_CREDITO = "cartao_credito"
    DINHEIRO = "dinheiro"


class CategoryType(str, enum.Enum):
    RECEITA = "receita"
    DESPESA = "despesa"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    senha_hash = Column(String(255), nullable=False)

    contas = relationship("Account", back_populates="usuario")
    transacoes = relationship("Transaction", back_populates="usuario")


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    tipo = Column(Enum(AccountType), nullable=False)
    saldo_inicial = Column(Float, default=0.0)
    usuario_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    usuario = relationship("User", back_populates="contas")
    transacoes = relationship("Transaction", back_populates="conta")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    tipo = Column(Enum(CategoryType), nullable=False)
    limite_orcamento = Column(Float, nullable=True)

    transacoes = relationship("Transaction", back_populates="categoria")


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(255), nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(Enum(TransactionType), nullable=False)
    data = Column(DateTime, default=datetime.utcnow, nullable=False)
    usuario_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    conta_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    compartilhada = Column(Boolean, default=False)
    parcelado = Column(Boolean, default=False)
    numero_parcelas = Column(Integer, nullable=True)
    parcela_atual = Column(Integer, nullable=True)

    usuario = relationship("User", back_populates="transacoes")
    conta = relationship("Account", back_populates="transacoes")
    categoria = relationship("Category", back_populates="transacoes")
