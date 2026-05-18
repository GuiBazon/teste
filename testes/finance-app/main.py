from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import init_db
from routers import users, accounts, categories, transactions, orcamento, export

app = FastAPI(
    title="Finance App",
    description="Sistema de financas pessoais e familiar compartilhado",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    init_db()


app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(categories.router)
app.include_router(transactions.router)
app.include_router(orcamento.router)
app.include_router(export.router)

app.mount("/", StaticFiles(directory="templates", html=True), name="frontend")
