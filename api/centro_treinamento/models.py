from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from api.contrib.models import BaseModel

if TYPE_CHECKING:
    from api.atleta.models import AtletaModel

from api.contrib.models import BaseModel


class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'

    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)

    atletas: Mapped[list["AtletaModel"]] = relationship(
        back_populates="centro_treinamento", 
        lazy="selectin"
    )

    def __repr__(self) -> str:
        return f"<CentroTreinamento(nome={self.nome}, uuid={self.id})>"