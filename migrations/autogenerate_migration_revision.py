from migrations import upgrade_model, downgrade_model, alc, AlembicConfig, schema_down, schema_up
from contextlib import contextmanager
import argparse


@contextmanager
def db_with_deps():
    try:
        schema_up()
        upgrade_model()
        yield
    finally:
        downgrade_model()
        schema_down()


def generate_revision(message="new revision"):
    with db_with_deps() as db:
        alc.revision(AlembicConfig("alembic.ini"),
                     message=message,
                     autogenerate=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a revision based on the model in vder_scheduler")
    parser.add_argument('revision_message', type=str, help='message for the revision')
    args = parser.parse_args()
    generate_revision(message=args.revision_message)

