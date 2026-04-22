from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from api.categorias.schemas import CategoriaIn, CategoriaOut
from api.categorias.models import CategoriaModel
from api.contrib.dependencies import DatabaseDependency


router = APIRouter()

@router.post('/', summary='Criar uma nova Categoria', status_code=status.HTTP_201_CREATED, response_model=CategoriaOut)
async def post(db_session: DatabaseDependency, categoria_in: CategoriaIn) -> CategoriaOut:

    try:
        categoria_model = CategoriaModel(**categoria_in.model_dump())
    
        db_session.add(categoria_model)
        await db_session.commit()
        await db_session.refresh(categoria_model)

        return categoria_model
    
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, detail=f'Já existe uma categoria cadastrada com o nome: {categoria_in.nome}')
    
@router.get('/', summary='Consultar todas as Categorias', status_code=status.HTTP_200_OK, response_model=list[CategoriaOut])
async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias = (await db_session.execute(select(CategoriaModel))).scalars().all()
    return categorias

@router.get('/{id}', summary='Consulta uma Categoria pelo id', status_code=status.HTTP_200_OK, response_model=CategoriaOut)
async def get(id: int, db_session: DatabaseDependency) -> CategoriaOut:
    categoria = (await db_session.execute(select(CategoriaModel).filter_by(pk_id=id))).scalars().first()

    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Categoria não encontrada no id: {id}')
    
    return categoria