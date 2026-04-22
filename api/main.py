from fastapi import FastAPI
from api.router import api_router

app = FastAPI(
    title='Gestão de Atletas API',
    version='0.1.0',
    description='Sistema de Gestão de Atletas - API de gerenciamento de atletas desenvolvida utilizando FastAPI, SQLAlchemy e PostgreSQL.',
    contact={
        "name": "Lucas Santos",
        "url": "https://github.com/lucas-glsantos/gestao-atletas-api.git",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)


app.include_router(api_router)
