from sqlalchemy import Column, Integer, ForeignKey

from orm.models.main import Base


class LinkChainsProtocolsPoolsAddresses(Base):

    __tablename__ = 'l_chains_protocols_pools_addresses'

    l_chain_protocol_pool_address_id = Column(Integer, primary_key=True)
    # ---
    l_address_chain_id = Column(Integer, ForeignKey('l_addresses_chains.l_address_chain_id'), nullable=False)
    l_address_pool_id = Column(Integer, ForeignKey('l_addresses_pools.l_address_pool_id'), nullable=False)
    l_chain_protocol_id = Column(Integer, ForeignKey('l_chains_protocols.l_chain_protocol_id'), nullable=False)
