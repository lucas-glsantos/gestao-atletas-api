"""
Schemas para o módulo de centro de treinamento.

Este módulo define os modelos de dados (schemas) utilizados para validação e documentação das operações relacionadas aos centros de treinamento.

Classes:
    CentroTreinamentoIn: Schema para entrada de dados de um centro de treinamento.
    CentroTreinamentoOut: Schema para saída de dados de um centro de treinamento, incluindo o identificador.
    CentroTreinamentoAtleta: Schema para exibir apenas o centro de treinamento associado a um atleta.
"""

from typing import Annotated
from pydantic import Field
from api.contrib.schemas import BaseSchema, OutMixin

class CentroTreinamentoBase(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', examples=['CT King'], max_length=50)]

class CentroTreinamentoIn(CentroTreinamentoBase):
    endereco: Annotated[str, Field(description='Endereço do CT', examples=['Rua X, 123'], max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do CT', examples=['Saitama'], max_length=30)]

class CentroTreinamentoOut(CentroTreinamentoIn, OutMixin):
    pass

class CentroTreinamentoAtleta(CentroTreinamentoBase):
    # Usado para exibição resumida dentro do AtletaOut
    pass
