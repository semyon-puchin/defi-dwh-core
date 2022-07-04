from sqlalchemy import Column, Integer, ForeignKey

from orm.models.main import Base


class LinkChainsProtocols(Base):

    __tablename__ = 'l_chains_protocols'

    l_chain_protocol_id = Column(Integer, primary_key=True)
    # ---
    h_chain_id = Column(Integer, ForeignKey('h_chains.h_chain_id'), nullable=False)
    h_protocol_id = Column(Integer, ForeignKey('h_protocols.h_protocol_id'), nullable=False)
