from migrations import upgrade_model, downgrade_model, alc, AlembicConfig
from alembic.autogenerate.api import AutogenContext
from alembic.autogenerate.render import _render_cmd_body
from src.bind import engine
from src.settings import postgres_schema
import pytest
from structlog import get_logger
logger = get_logger(module=__name__)


def test_migration(schema):
    # start with first revision
    upgrade_model(revision="8e9d2dd2e8e8")
    # add data
    # with engine.connect() as con:
    #     for res in con.execute(f"SELECT * FROM information_schema.columns WHERE table_schema = '{postgres_schema}' AND table_name = 'darksky_hourly'"):
    #         print(res)
    with engine.connect() as con:
        con.execute(f"INSERT INTO {postgres_schema}.model(foo, bar)"
                    "VALUES ('Jazz', 'Hands')")
    # upgrade all the way to confirm it works
    upgrade_model()

    def verify_is_empty_revision(migration_context, __, directives):
        """Adapted from pytest-alembic test_model_definitions_match_ddl"""
        script = directives[0]

        migration_is_empty = script.upgrade_ops.is_empty()
        if not migration_is_empty:
            autogen_context = AutogenContext(migration_context)
            rendered_upgrade = _render_cmd_body(script.upgrade_ops, autogen_context)
            pytest.fail(
                "The models decribing the DDL of your database are out of sync with the set of "
                "steps described in the revision history. This usually means that someone has "
                "made manual changes to the database's DDL, or some model has been changed "
                "without also generating a migration to describe that change. The upgrade which "
                f"would have been generated would look like:\n {rendered_upgrade}")
        else:
            directives[:] = []

    # check that latest revision matches the model in src.model
    alc.revision(AlembicConfig("alembic.ini"),
                 message="test revision",
                 autogenerate=True,
                 process_revision_directives=verify_is_empty_revision,
                 )

    # downgrade back to initial
    downgrade_model("8e9d2dd2e8e8")
    # downgrade all the way
    downgrade_model()

