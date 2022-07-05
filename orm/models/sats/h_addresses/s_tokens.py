from sqlalchemy import Column, Integer, Text, ForeignKey

from orm.models.main import Base


class SatelliteTokens(Base):

    __tablename__ = 's_tokens'

    s_token_id = Column(Integer, primary_key=True)
    h_address_id = Column(Integer, ForeignKey('h_addresses.h_address_id'), nullable=False)
    # ---
    s_token_symbol = Column(Text, nullable=False)
    s_token_decimals = Column(Integer, nullable=False)
