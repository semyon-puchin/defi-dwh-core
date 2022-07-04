from sqlalchemy import Column, Integer, Text, Boolean, DateTime, Enum

from orm.consts.revenue_type import RevenueType
from orm.models.main import Base


class HubPools(Base):

    __tablename__ = 'h_pools'

    h_pool_id = Column(Integer, primary_key=True)
    # ---
    h_pool_label = Column(Text, nullable=False)
    h_revenue_type = Column(Enum(RevenueType), nullable=False)
    h_is_impermanent_loss = Column(Boolean, nullable=False)

    h_pool_load_ts = Column(DateTime, nullable=False)
