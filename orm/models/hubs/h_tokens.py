from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func

from orm.models.main import Base


class HubTokens(Base):

    __tablename__ = 'h_tokens'

    h_token_id = Column(Integer, primary_key=True)  # PK
    h_token_symbol = Column(Text, unique=True, nullable=False)
    h_token_decimals = Column(Integer, nullable=False)
    h_token_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
