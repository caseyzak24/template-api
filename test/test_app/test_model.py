import pytest
from src.model import Model
from src.settings import postgres_schema
from src.bind import session_scope


def test_table_exists(db):
    with session_scope() as sesh:
        assert sesh.execute(
            "SELECT EXISTS ( "
            "SELECT 1 "
            "FROM   information_schema.tables "
            f"WHERE table_schema = '{postgres_schema}' "
            f"AND table_name = '{Model.__tablename__}' "
            ");"
        ).fetchone() == (1,)
