from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api.contrib.models import BaseModel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.atleta.models import AtletaModel


class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'


    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    # Relacionamento com AtletaModel
    atletas: Mapped[list["AtletaModel"]] = relationship(
        back_populates="categoria",
        lazy="selectin",
    )


    def __repr__(self) -> str:
        return f"<Categoria(nome={self.nome}, uuid={self.id})>"