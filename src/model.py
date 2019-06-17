from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import validates
from sqlalchemy import Column, Integer, String, UniqueConstraint, DateTime
from alembic.config import Config as AlembicConfig
import alembic.command as alc


Base = declarative_base()


class Model(Base):

    __tablename__ = 'model'
    __table_args__ = (
        UniqueConstraint('foo', 'bar'),
        {'schema': 'baz'}
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    time_created = Column(DateTime, server_default=func.now(), nullable=False)

    foo = Column(String, nullable=False)
    bar = Column(String, nullable=False)

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    @validates('foo')
    def validate_foo(self, key, foo):
        if foo not in ('spam', 'eggs'):
            raise ValueError('foo must be either "spam" or "eggs"')
        return foo


def setup(revision='head'):
    alc.upgrade(AlembicConfig('alembic.ini'), revision)


def teardown():
    alc.downgrade(AlembicConfig('alembic.ini'), 'base')
