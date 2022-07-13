from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func

from orm.models.main import Base


class HubSupportAddresses(Base):

    __tablename__ = 'h_supp_addresses'

    h_supp_address_id = Column(Integer, primary_key=True)  # PK
    h_supp_address = Column(Text, unique=True, nullable=False)
    h_supp_address_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
