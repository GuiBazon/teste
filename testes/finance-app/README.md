# 💰 Finance App

Sistema de finanças pessoais e familiar compartilhado. API REST com interface Single Page Application (SPA) responsiva.

- **Cadastro** de usuários, contas e categorias
- **Transações** com suporte a parcelamento no cartão de crédito
- **Transações compartilhadas** visíveis para toda a família
- **Dashboard** com resumo mensal (receitas, despesas, saldo)
- **Orçamento** por categoria com barras de progresso
- **Exportação** de relatório CSV mensal

---

## Tecnologias

| Camada | Tecnologia |
|--------|-----------|
| Backend | Python 3.14+, FastAPI, Uvicorn |
| ORM | SQLAlchemy 2.x |
| Banco | SQLite (zero configuração) |
| Autenticação | JWT (python-jose + passlib/bcrypt) |
| Validação | Pydantic v2 |
| Frontend | HTML5 + JavaScript Vanilla |
| Estilo | TailwindCSS (via CDN) |
| Templates | FastAPI StaticFiles |

---

## Estrutura do Projeto

```
finance-app/
├── main.py                  # Servidor FastAPI (rotas + static)
├── database.py              # Conexão SQLite + engine
├── models.py                # Modelos ORM (4 tabelas)
├── schemas.py               # Schemas Pydantic (validação)
├── requirements.txt         # Dependências
├── finance.db               # Banco SQLite (criado automaticamente)
├── templates/
│   └── index.html           # SPA completa (HTML + JS + Tailwind)
└── routers/
    ├── users.py             # CRUD usuários + login JWT
    ├── accounts.py          # CRUD contas bancárias
    ├── categories.py        # CRUD categorias
    ├── transactions.py      # CRUD transações + parcelamento
    ├── orcamento.py         # Dashboard de orçamento
    └── export.py            # Exportação CSV
```

---

## Banco de Dados

### 4 tabelas relacionadas

**users** — armazena os usuários do sistema
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER (PK) | Identificador único |
| nome | VARCHAR(100) | Nome do usuário |
| email | VARCHAR(100) | Email único (login) |
| senha_hash | VARCHAR(255) | Hash bcrypt da senha |

**accounts** — contas bancárias de cada usuário
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER (PK) | Identificador único |
| nome | VARCHAR(100) | Nome da conta (ex: "Nubank") |
| tipo | ENUM | conta_corrente / cartao_credito / dinheiro |
| saldo_inicial | FLOAT | Saldo inicial da conta |
| usuario_id | INTEGER (FK → users.id) | Dono da conta |

**categories** — categorias de receitas e despesas
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER (PK) | Identificador único |
| nome | VARCHAR(100) | Nome da categoria |
| tipo | ENUM | receita / despesa |
| limite_orcamento | FLOAT (nullable) | Limite mensal de gasto |

**transactions** — registro financeiro
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER (PK) | Identificador único |
| descricao | VARCHAR(255) | Descrição da transação |
| valor | FLOAT | Valor |
| tipo | ENUM | receita / despesa |
| data | DATETIME | Data da transação |
| usuario_id | INTEGER (FK → users.id) | Dono |
| conta_id | INTEGER (FK → accounts.id) | Conta vinculada |
| categoria_id | INTEGER (FK → categories.id) | Categoria |
| compartilhada | BOOLEAN | Visível para todos? |
| parcelado | BOOLEAN | É compra parcelada? |
| numero_parcelas | INTEGER (nullable) | Total de parcelas |
| parcela_atual | INTEGER (nullable) | Número da parcela atual |

---

## Instalação

### Pré-requisitos

- Python 3.10 ou superior instalado
- Pip (gerenciador de pacotes do Python)

### Passo a passo

```bash
# 1. Acesse a pasta do projeto
cd finance-app

# 2. Crie um ambiente virtual (recomendado)
python -m venv venv

# 3. Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux / Mac:
source venv/bin/activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Inicie o servidor
uvicorn main:app --reload
```

O servidor estará disponível em **http://localhost:8000**

---

## Como Usar

### 1. Acessar a interface

Abra o navegador em `http://localhost:8000`

### 2. Cadastrar dados iniciais (via Swagger)

Acesse `http://localhost:8000/docs` e use a interface Swagger para:

1. **POST /api/users/register** — cadastre 2 ou 3 usuários da família
2. **POST /api/categories/** — crie categorias como "Alimentação", "Transporte", "Salário"
3. **POST /api/accounts/** — crie contas como "Nubank", "Itaú", "Carteira"

### 3. Usar o sistema

1. Volte para `http://localhost:8000`
2. Selecione seu usuário no dropdown e clique **Entrar**
3. Use o formulário **Nova Transação** para registrar receitas e despesas
4. Marque "Compra Parcelada?" para dividir em várias parcelas
5. Marque "Compartilhar com a Casa?" para transações visíveis a todos
6. Acompanhe os cards de resumo e as barras de orçamento
7. Clique em **Baixar Relatório (CSV)** para exportar o mês

---

## API — Rotas Disponíveis

### Usuários (`/api/users`)

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| POST | `/register` | Cadastrar novo usuário | ❌ |
| POST | `/login` | Login (email + senha) | ❌ |
| POST | `/login-dev/{id}` | Login rápido por ID (dev) | ❌ |
| GET | `/` | Listar todos os usuários | ❌ |
| GET | `/me` | Dados do usuário logado | ✅ |
| PUT | `/{id}` | Atualizar próprio perfil | ✅ |
| DELETE | `/{id}` | Deletar própria conta | ✅ |

### Contas (`/api/accounts`)

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| POST | `/` | Criar conta | ✅ |
| GET | `/` | Listar contas do usuário | ✅ |
| GET | `/{id}` | Detalhar conta | ✅ |
| PUT | `/{id}` | Atualizar conta | ✅ |
| DELETE | `/{id}` | Deletar conta | ✅ |

### Categorias (`/api/categories`)

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| POST | `/` | Criar categoria | ✅ |
| GET | `/` | Listar categorias | ✅ |
| GET | `/{id}` | Detalhar categoria | ✅ |
| PUT | `/{id}` | Atualizar categoria | ✅ |
| DELETE | `/{id}` | Deletar categoria | ✅ |

### Transações (`/api/transactions`)

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| POST | `/` | Criar transação (ou parcelas) | ✅ |
| GET | `/` | Listar transações visíveis | ✅ |
| GET | `/{id}` | Detalhar transação | ✅ |
| PUT | `/{id}` | Atualizar transação | ✅ |
| DELETE | `/{id}` | Deletar transação | ✅ |

### Orçamento (`/api/orcamento`)

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| GET | `/{ano}/{mes}` | Dashboard de orçamento mensal | ✅ |

### Exportação (`/api/exportar`)

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| GET | `/{user_id}/{ano}/{mes}` | Download CSV do mês | ✅ |

---

## Estrutura do Código

### Fluxo de uma requisição

```
Navegador (index.html)
    │  fetch() com Bearer token
    ▼
FastAPI (main.py)
    │  Roteia para o módulo adequado
    ▼
Router (ex: transactions.py)
    │  Valida payload com Pydantic
    ▼
SQLAlchemy ORM (models.py)
    │  Executa query no SQLite
    ▼
SQLite (finance.db)
    │  Retorna dados
    ▼
Resposta JSON → Navegador renderiza com JS
```

### Autenticação JWT

1. Usuário faz login → recebe `access_token` (JWT com 24h de validade)
2. Token é armazenado no `sessionStorage` do navegador
3. Toda requisição para rotas protegidas envia `Authorization: Bearer <token>`
4. `get_current_user()` decodifica o token e retorna o usuário logado

### Regras de negócio implementadas

- **Transação compartilhada**: se `compartilhada=true`, fica visível para todos os usuários logados; se `false`, apenas para o dono
- **Parcelamento**: se `parcelado=true` e `numero_parcelas >= 2`, o sistema calcula `valor / N` e cria N transações com datas avançando 1 mês
- **Orçamento**: compara `SUM(valor)` das despesas do mês com `limite_orcamento` de cada categoria; barras coloridas (verde < 50%, amarelo 50-80%, vermelho > 80%)
- **Exportação**: busca transações privadas + compartilhadas do mês e retorna CSV com `StreamingResponse`
