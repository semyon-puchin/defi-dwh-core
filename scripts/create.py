from cfg.engine import db_engine
from main import Base


if __name__ == '__main__':
    Base.metadata.create_all(db_engine)
