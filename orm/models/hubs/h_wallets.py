from sqlalchemy import Column, Integer, Text, DateTime

from orm.models.main import Base


class HubWallets(Base):

    __tablename__ = 'h_wallets'

    h_wallet_id = Column(Integer, primary_key=True)
    # ---
    h_wallet_label = Column(Text, unique=True, nullable=False)
    h_wallet_notional = Column(Text, nullable=False)

    h_wallet_load_ts = Column(DateTime, nullable=False)
