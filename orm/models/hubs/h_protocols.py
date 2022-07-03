from enum import Enum
from sqlalchemy import Column, Integer, Text, DateTime

from orm.consts.protocol_type import ProtocolType
from main import Base


class HubProtocols(Base):

    __tablename__ = 'h_protocols'

    h_protocol_id = Column(Integer, primary_key=True)
    # ---
    h_protocol_name = Column(Text, unique=True, nullable=False)
    h_protocol_type = Column(Enum(ProtocolType), nullable=False)

    h_protocol_load_ts = Column(DateTime, nullable=False)
