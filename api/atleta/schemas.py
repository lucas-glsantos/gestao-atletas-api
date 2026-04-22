from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from api.contrib.schemas import BaseSchema, OutMixin
from api.atleta.enums import SexoEnum
from api.categorias.schemas import CategoriaOut

from api.centro_treinamento.schemas import CentroTreinamentoAtleta


class AtletaBase(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', examples=['Joao'], max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples=['12345678900'], max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=[25])]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=[75.5])]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', examples=[1.70])]
    sexo: Annotated[SexoEnum, Field(description='Sexo do atleta', examples=['M'], max_length=1)]

class AtletaIn(AtletaBase):
    categoria_id: int
    centro_treinamento_id: int

class AtletaOut(AtletaBase, OutMixin):
    # Retorna dados completos dos relacionamentos
    categoria: CategoriaOut
    centro_treinamento: CentroTreinamentoAtleta

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, max_length=50)]
    idade: Annotated[Optional[int], Field(None)]
    peso: Annotated[Optional[PositiveFloat], Field(None)]
    altura: Annotated[Optional[PositiveFloat], Field(None)]