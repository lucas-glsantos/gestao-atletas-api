from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey, Numeric, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.contrib.models import BaseModel
from api.atleta.enums import SexoEnum

if TYPE_CHECKING:
    from api.categorias.models import CategoriaModel
    from api.centro_treinamento.models import CentroTreinamentoModel

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    
    peso: Mapped[Decimal] = mapped_column(Numeric(5, 2),nullable=False,)
    altura: Mapped[Decimal] = mapped_column(Numeric(3, 2),nullable=False,)
    sexo: Mapped[SexoEnum] = mapped_column(SAEnum(SexoEnum, name="sexo"), nullable=False)

    # FK apontando para PK
    categoria_id: Mapped[int] = mapped_column(
        ForeignKey("categorias.pk_id", ondelete="CASCADE"),
        index=True, 
        nullable=False,
    )
    
    centro_treinamento_id: Mapped[int] = mapped_column(
        ForeignKey("centros_treinamento.pk_id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    # Relacionamentos
    categoria: Mapped["CategoriaModel"] = relationship(
        back_populates="atletas", 
        lazy="selectin",
    )
    
    centro_treinamento: Mapped["CentroTreinamentoModel"] = relationship(
        back_populates="atletas",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<Atleta(nome={self.nome}, cpf={self.cpf}, uuid={self.id})>"
    