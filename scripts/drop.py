from cfg.engine import db_engine
from orm.models.main import Base


if __name__ == '__main__':
    Base.metadata.drop_all(db_engine)