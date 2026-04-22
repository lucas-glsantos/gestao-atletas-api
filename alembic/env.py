from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from api.contrib.models import BaseModel
from api.configs.settings import settings
from api.atleta.models import AtletaModel
from api.categorias.models import CategoriaModel
from api.centro_treinamento.models import CentroTreinamentoModel


# Configuração base do Alembic
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata usada pelo autogenerate
target_metadata = BaseModel.metadata


# Força Alembic a usar DATABASE_URL_SYNC (psycopg)
if not settings.DATABASE_URL_SYNC:
    raise RuntimeError("DATABASE_URL_SYNC Não foi definida")

if "postgresql" not in settings.DATABASE_URL_SYNC:
    raise RuntimeError("DATABASE_URL_SYNC Inválida")

config.set_main_option("sqlalchemy.url", settings.DATABASE_URL_SYNC)


# Migrations OFFLINE
def run_migrations_offline():
    """
    Executa migrations no modo offline.
    Não cria conexão com o banco.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

# Migrations ONLINE
def run_migrations_online():
    """
    Executa migrations no modo online.
    Usa engine SINCRONO (psycopg2).
    """
    # Garante que a engine use a URL injetada pelo Docker
    configuration = config.get_section(config.config_ini_section) or {}
    configuration["sqlalchemy.url"] = settings.DATABASE_URL_SYNC

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    print(f"Rodando migrations com: {settings.DATABASE_URL_SYNC}")

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

# Dispatcher
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()