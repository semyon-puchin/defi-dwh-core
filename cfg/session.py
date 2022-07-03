from sqlalchemy.orm import sessionmaker
from .engine import db_engine, test_engine

MainSession = sessionmaker(db_engine)
TestSession = sessionmaker(test_engine)