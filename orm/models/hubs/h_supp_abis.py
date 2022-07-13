from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func

from orm.models.main import Base


class HubSupportAbis(Base):

    __tablename__ = 'h_supp_abis'

    h_supp_abi_id = Column(Integer, primary_key=True)  # PK
    h_supp_abi_list = Column(Text, unique=True, nullable=False)
    h_supp_abi_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
