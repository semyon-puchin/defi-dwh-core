from sqlalchemy import Column, Integer, Text, DateTime, Enum
from sqlalchemy.sql import func

from orm.consts.protocol_type import ProtocolType
from orm.models.main import Base


class HubProtocols(Base):

    __tablename__ = 'h_protocols'

    h_protocol_id = Column(Integer, primary_key=True)  # PK
    h_protocol_name = Column(Text, unique=True, nullable=False)
    h_protocol_type = Column(Enum(ProtocolType), nullable=False)
    h_protocol_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
