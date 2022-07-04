from sqlalchemy import Column, Integer, Text, ForeignKey

from orm.models.main import Base


class SatelliteWallets(Base):

    __tablename__ = 's_wallets'

    s_wallet_id = Column(Integer, primary_key=True)
    h_address_id = Column(Integer, ForeignKey('h_addresses.h_address_id'), nullable=False)
    # ---
    s_wallet_label = Column(Text, unique=True, nullable=False)
    s_wallet_notional = Column(Text, nullable=False)
