import pytest
from src.bind import engine, session_scope
from src.model import metadata, Model
import typing as t
from migrations import schema_up, schema_down


@pytest.fixture(scope='session')
def some_fixture():
    return NotImplemented


@pytest.fixture(scope="session")
def schema():
    try:
        schema_up()
        yield
    finally:
        schema_down()


@pytest.fixture(scope='function')
def db(schema):
    try:
        metadata.create_all(engine)
        yield
    finally:
        engine.dispose()
        metadata.drop_all(engine)


@pytest.fixture(scope='function')
def populated_db(db, test_model):
    populate_db(model=test_model)


# note this is "unfixtured" so that you can use it while sandboxing or if you are setting up a test env
def populate_db(model: t.Optional[dict] = None):
    if not model:
        model = _model
    with session_scope() as sesh:
        sesh.add(Model(
            foo=model["foo"],
            bar=model["bar"]))


@pytest.fixture(scope='module')
def test_model() -> dict:
    return _model


_model = {"foo": "jazz", "bar": "hands"}


@pytest.fixture(scope='module')
def another_fixture1(another_fixture2, test_model) -> dict:
    return {}


@pytest.fixture(scope='session')
def another_fixture2() -> list:
    return []