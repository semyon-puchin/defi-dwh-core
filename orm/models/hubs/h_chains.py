from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func

from orm.models.main import Base


class HubChains(Base):

    __tablename__ = 'h_chains'

    h_chain_id = Column(Integer, primary_key=True)  # PK
    h_network_name = Column(Text, unique=True, nullable=False)
    h_network_id = Column(Integer, unique=True, nullable=False)
    h_network_endpoint = Column(Text, unique=True, nullable=False)
    h_network_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
