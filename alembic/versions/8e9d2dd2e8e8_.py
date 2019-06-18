"""empty message

Revision ID: 8e9d2dd2e8e8
Revises: 
Create Date: 2019-06-18 01:48:15.982317

auto-generated with `alembic revision --autogenerate`
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e9d2dd2e8e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('create schema baz')
    op.create_table(
        'model',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('time_created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('foo', sa.String(), nullable=False),
        sa.Column('bar', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('foo', 'bar'),
        schema='baz'
    )


def downgrade():
    op.drop_table('model', schema='baz')
    op.execute(f'drop schema baz')
