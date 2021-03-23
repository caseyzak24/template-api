from alembic import command as alc
from alembic.config import Config as AlembicConfig
from src.bind import engine
from src.settings import postgres_schema
from structlog import get_logger
logger = get_logger(module=__name__)


def upgrade_model(revision="head"):
    alc.upgrade(AlembicConfig("alembic.ini"), revision)


def downgrade_model(revision="base"):
    alc.downgrade(AlembicConfig("alembic.ini"), revision)


def schema_up():
    with engine.connect() as con:
        con.execute(f"CREATE SCHEMA IF NOT EXISTS {postgres_schema}")
    logger.info("created schema")


def schema_down():
    with engine.connect() as con:
        con.execute(f"DROP SCHEMA IF EXISTS {postgres_schema} CASCADE")
    logger.info("dropped schema")
