import pytest

from sqlalchemy_utils import database_exists, drop_database, create_database

from cfg.engine import db_url, db_engine
from cfg.session import Session

from orm.models.main import Base


@pytest.mark.order(2)
@pytest.fixture(scope='class', autouse=True)
def clear_db_before_usage():
    if database_exists(db_url):
        drop_database(db_url)
    create_database(db_url)
    Base.metadata.create_all(db_engine)


@pytest.mark.order(1)
@pytest.fixture(scope='class')
def session():
    session = Session()
    yield session
    session.close()
