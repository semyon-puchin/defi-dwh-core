from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean

from orm.models.main import Base


class SatelliteAddressesAbisTokensProtocolsChains(Base):

    __tablename__ = 's_addresses_abis_tokens_protocols_chains'

    s_address_abi_token_protocol_chain_id = Column(Integer, primary_key=True)  # PK
    l_address_abi_token_protocol_chain_id = Column(Integer, ForeignKey('l_addresses_abis_tokens_protocols_chains.l_address_abi_token_protocol_chain_id'), nullable=False)
    s_address_abi_token_protocol_chain_name = Column(Text, nullable=False)
    s_address_abi_token_protocol_chain_is_impermanent_loss = Column(Boolean, nullable=False)
