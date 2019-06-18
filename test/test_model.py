import pytest
from src.model import setup, teardown, Model
from src.bind import session_scope


@pytest.fixture()
def db():
    setup()
    yield
    teardown()


def test_setup(db):
    with session_scope() as sesh:
        assert sesh.execute(
            "SELECT EXISTS ( "
                "SELECT 1 "
                "FROM   information_schema.tables "
               f"WHERE  table_name = '{Model.__tablename__}' "
           ");"
        ).fetchone() == (1,)
