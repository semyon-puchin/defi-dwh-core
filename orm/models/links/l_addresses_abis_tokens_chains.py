from sqlalchemy import Column, Integer, ForeignKey

from orm.models.main import Base


class LinkAddressesAbisTokensChains(Base):

    __tablename__ = 'l_addresses_abis_tokens_chains'

    l_address_abi_token_chain_id = Column(Integer, primary_key=True)  # PK
    l_address_abi_chain_id = Column(Integer, ForeignKey('l_addresses_abis_chains.l_address_abi_chain_id'), nullable=False)
    h_token_id = Column(Integer, ForeignKey('h_tokens.h_token_id'), nullable=False)
