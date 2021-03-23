from alembic import op
import sqlalchemy as sa
from src.settings import postgres_schema


# revision identifiers, used by Alembic.
revision = '8e9d2dd2e8e8'
down_revision = None
branch_labels = None
depends_on = None

schema = postgres_schema


def upgrade():
    op.execute(f"CREATE SCHEMA IF NOT EXISTS {postgres_schema}")
    op.create_table(
        'model',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('time_created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('foo', sa.String(), nullable=False),
        sa.Column('bar', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('foo', 'bar'),
        schema=schema
    )


def downgrade():
    op.drop_table('model', schema=schema)
    op.execute(f"DROP SCHEMA IF EXISTS {postgres_schema} CASCADE")
