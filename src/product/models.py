from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Text,\
    FLOAT, ForeignKey
from datetime import datetime
from sqlalchemy import MetaData
from auth.models import user as user_model

metadata = MetaData()


product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50), nullable=False),
    Column("description", Text, nullable=False),
    Column("price", FLOAT, nullable=False),
    Column("added_at", TIMESTAMP, nullable=False, default=datetime.utcnow),
    Column("seller_id", Integer, ForeignKey(user_model.c.id), nullable=False))
