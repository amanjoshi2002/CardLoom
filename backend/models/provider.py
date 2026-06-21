from sqlalchemy import Column, Integer, String
from database import Base

class Provider(Base):
    __tablename__ = "providers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    api_key = Column(String, nullable=False)


