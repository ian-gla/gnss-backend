import sqlalchemy as sa

# import geoalchemy2 as ga
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase


schema = "gnss"

metadata_obj = MetaData(schema=schema)


class Base(DeclarativeBase):
    metadata = metadata_obj


class Users(Base):
    __tablename__ = "users"

    id = sa.Column("id", sa.Integer, primary_key=True)
    email = sa.Column("email", sa.String, nullable=False)
