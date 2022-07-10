from sqlalchemy import Column, Integer, ForeignKey

from orm.models.main import Base


class LinkAddressesChains(Base):

    __tablename__ = 'l_addresses_chains'

    l_address_chain_id = Column(Integer, primary_key=True)  # PK
    h_address_id = Column(Integer, ForeignKey('h_addresses.h_address_id'), nullable=False)
    h_chain_id = Column(Integer, ForeignKey('h_chains.h_chain_id'), nullable=False)
