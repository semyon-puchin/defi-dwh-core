from sqlalchemy import Column, Integer, ForeignKey

from orm.models.main import Base


class LinkAddressesAbisChains(Base):

    __tablename__ = 'l_addresses_abis_chains'

    l_address_abi_chain_id = Column(Integer, primary_key=True)  # PK
    l_address_chain_id = Column(Integer, ForeignKey('l_addresses_chains.l_address_chain_id'), nullable=False)
    h_abi_id = Column(Integer, ForeignKey('h_abis.h_abi_id'), nullable=False)
