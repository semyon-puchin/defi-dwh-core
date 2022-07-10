from sqlalchemy import Column, Integer, ForeignKey

from orm.models.main import Base


class LinkAddressesWallets(Base):

    __tablename__ = 'l_addresses_wallets'

    l_address_wallet_id = Column(Integer, primary_key=True)
    # ---
    h_address_id = Column(Integer, ForeignKey('h_addresses.h_address_id'), nullable=False)
    h_wallet_id = Column(Integer, ForeignKey('h_wallets.h_wallet_id'), nullable=False)
