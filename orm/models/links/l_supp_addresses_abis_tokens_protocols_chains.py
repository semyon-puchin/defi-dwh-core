from sqlalchemy import Column, Integer, ForeignKey, Text

from orm.models.main import Base


class LinkSupportAddressesAbisTokensProtocolsChains(Base):

    __tablename__ = 'l_supp_addresses_abis_tokens_protocols_chains'

    l_supp_address_abi_token_protocol_chain_id = Column(Integer, primary_key=True)  # PK
    h_supp_address_id = Column(Integer, ForeignKey('h_supp_addresses.h_supp_address_id'), nullable=False)
    h_supp_abi_id = Column(Integer, ForeignKey('h_supp_abis.h_supp_abi_id'), nullable=False)
    l_address_abi_token_protocol_chain_id = Column(Integer, ForeignKey('l_addresses_abis_tokens_protocols_chains.l_address_abi_token_protocol_chain_id'), nullable=False)
    l_supp_address_abi_token_protocol_chain_n = Column(Text, nullable=False)
