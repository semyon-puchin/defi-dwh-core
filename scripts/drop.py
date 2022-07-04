from cfg import engine
from main import Base


if __name__ == '__main__':
    Base.metadata.drop_all(engine)