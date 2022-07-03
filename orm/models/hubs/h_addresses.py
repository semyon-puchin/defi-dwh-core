from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.orm import relationship

from main import Base


class HubAddresses(Base):

    __tablename__ = 'h_addresses'

    h_address_id = Column(Integer, primary_key=True)
    # ---
    h_address = Column(Text, unique=True, nullable=False)

    h_address_load_ts = Column(DateTime, nullable=False)
