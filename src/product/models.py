from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text,\
    FLOAT, ForeignKey
from datetime import datetime
from sqlalchemy import MetaData
from auth.models import user as user_model

metadata = MetaData()


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(FLOAT, nullable=False)
    added_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    seller_id = Column(Integer, ForeignKey(user_model.c.id))

    @property
    def serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "added_at": self.added_at,
            "seller_id": self.seller_id
        }
