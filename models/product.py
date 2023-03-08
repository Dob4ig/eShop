from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Text
from datetime import datetime
from models.models import metadata


product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("description", Text, nullable=False),
    Column("added_at", TIMESTAMP, nullable=False, default=datetime.utcnow)
)
