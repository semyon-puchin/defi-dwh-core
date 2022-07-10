from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func

from orm.models.main import Base


class HubAbis(Base):

    __tablename__ = 'h_abis'

    h_abi_id = Column(Integer, primary_key=True)  # PK
    h_abi_list = Column(Text, unique=True, nullable=False)
    h_abi_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
