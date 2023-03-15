
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text,\
    ForeignKey
from datetime import datetime
from database import Base


class VerifyQuee(Base):
    __tablename__ = 'verify_quee'
    id = Column(Integer, primary_key=True)
    shop_name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    image_path = Column(String(100))
    owner_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    added_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
