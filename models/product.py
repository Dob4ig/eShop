from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP
from datetime import datetime

metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, max_length=50),
    Column("description", String, nullable=False),
    Column("added_at", TIMESTAMP, nullable=False, default=datetime.utcnow)
)
