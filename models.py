from sqlalchemy import String,Integer,Column,Text
from database import Base
class users(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(20),nullable=False)
    email=Column(Text,unique=True)
    age=Column(Integer,nullable=True)
