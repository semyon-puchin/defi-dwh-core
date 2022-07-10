from sqlalchemy import Column, Integer, ForeignKey

from orm.models.main import Base


class LinkProtocolsChains(Base):

    __tablename__ = 'l_protocols_chains'

    l_protocol_chain_id = Column(Integer, primary_key=True)  # PK
    h_protocol_id = Column(Integer, ForeignKey('h_protocols.h_protocol_id'), nullable=False)
    h_chain_id = Column(Integer, ForeignKey('h_chains.h_chain_id'), nullable=False)
