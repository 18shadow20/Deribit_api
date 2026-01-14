from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    price = Column(Numeric(20, 8))
    timestamp = Column(Integer, index=True)


Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autoflush=False, bind=engine, expire_on_commit=False)




