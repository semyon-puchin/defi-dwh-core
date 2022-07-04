from sqlalchemy.orm import sessionmaker
from cfg.engine import db_engine

MainSession = sessionmaker(db_engine)
