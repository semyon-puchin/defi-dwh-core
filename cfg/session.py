from sqlalchemy.orm import sessionmaker
from .engine import db_engine

MainSession = sessionmaker(db_engine)
