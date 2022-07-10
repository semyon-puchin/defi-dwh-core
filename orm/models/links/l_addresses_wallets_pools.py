from sqlalchemy import Column, Integer, ForeignKey

from orm.models.main import Base


class LinkAddressesWalletsPools(Base):

    __tablename__ = 'l_addresses_wallets_pools'

    l_address_wallet_pool_id = Column(Integer, primary_key=True)
    # ---
    l_address_pool_id = Column(Integer, ForeignKey('l_addresses_pools.l_address_pool_id'), nullable=False)
    l_address_wallet_id = Column(Integer, ForeignKey('l_addresses_wallets.l_address_wallet_id'), nullable=False)
