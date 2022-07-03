from sqlalchemy import Column, Integer, Text, DateTime

from main import Base


class HubChains(Base):

    __tablename__ = 'h_chains'

    h_chain_id = Column(Integer, primary_key=True)
    # ---
    h_network = Column(Text, unique=True, nullable=False)
    h_network_id = Column(Integer, unique=True, nullable=False)

    h_chain_load_ts = Column(DateTime, nullable=False)
