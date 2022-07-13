from sqlalchemy.orm import sessionmaker
from cfg.engine import db_engine

Session = sessionmaker(db_engine)
