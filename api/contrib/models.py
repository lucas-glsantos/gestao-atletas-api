from datetime import datetime
from uuid import uuid4, UUID
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class BaseModel(DeclarativeBase):
    # PK para performance em joins (Clustered Index)
    pk_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # ID público para exposição na API
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), 
        default=uuid4, 
        nullable=False,
        unique=True,
        index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )