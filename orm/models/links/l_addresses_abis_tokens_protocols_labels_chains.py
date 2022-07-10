from sqlalchemy import Column, Integer, ForeignKey

from orm.models.main import Base


class LinkAddressesAbisTokensProtocolsLabelsChains(Base):

    __tablename__ = 'l_addresses_abis_tokens_protocols_labels_chains'

    l_address_abi_token_protocol_label_chain_id = Column(Integer, primary_key=True)  # PK

    l_address_abi_token_protocol_chain_id = Column(Integer, ForeignKey('l_addresses_abis_tokens_protocols_chains.l_address_abi_token_protocol_chain_id'), nullable=False)
    l_address_label_chain_id = Column(Integer, ForeignKey('l_addresses_labels_chains.l_address_label_chain_id'), nullable=False)
