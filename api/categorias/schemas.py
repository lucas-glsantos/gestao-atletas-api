from pydantic import Field
from typing import Annotated
from api.contrib.schemas import BaseSchema, OutMixin

class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', examples=['Scale'], max_length=50)]

class CategoriaOut(CategoriaIn, OutMixin):
    pass