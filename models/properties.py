from sqlalchemy import Boolean, Column, ForeignKey, Integer, String    
from storage.database_pg import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String )
    email = Column(String, unique=True)
    password = Column(String)
    phone = Column(String)