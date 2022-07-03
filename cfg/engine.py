from sqlalchemy import create_engine
import os
from urllib.parse import quote_plus

db_address = os.getenv('DB_ADDRESS', 'localhost')
db_user = os.getenv('DB_USER', '')
db_password = quote_plus(os.getenv('DB_PASSWORD', ''))
db_name = os.getenv('ORM_DB_NAME', '')

db_url = f'postgresql://{db_user}:{db_password}@{db_address}/{db_name}'
db_engine = create_engine(db_url)
