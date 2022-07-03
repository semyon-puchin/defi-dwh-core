from enum import Enum
from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey

from orm.consts.revenue_type import RevenueType
from main import Base


class SatellitePools(Base):

    __tablename__ = 's_pools'

    s_pool_id = Column(Integer, primary_key=True)
    h_address_id = Column(Integer, ForeignKey('h_addresses.h_address_id'), nullable=False)
    # ---
    s_pool_label = Column(Text, nullable=False)
    s_revenue_type = Column(Enum(RevenueType), nullable=False)
    s_is_impermanent_loss = Column(Boolean, nullable=False)
