from sqlalchemy import Column, Integer, ForeignKey

from orm.models.main import Base


class LinkAddressesLabelsChains(Base):

    __tablename__ = 'l_addresses_labels_chains'

    l_address_label_chain_id = Column(Integer, primary_key=True)  # PK
    l_address_chain_id = Column(Integer, ForeignKey('l_addresses_chains.l_address_chain_id'), nullable=False)
    h_label_id = Column(Integer, ForeignKey('h_labels.h_label_id'), nullable=False)
