from sqlalchemy import Column, Integer, ForeignKey

from orm.models.main import Base


class LinkAddressesPools(Base):

    __tablename__ = 'l_addresses_pools'

    l_address_pool_id = Column(Integer, primary_key=True)
    # ---
    h_address_id = Column(Integer, ForeignKey('h_addresses.h_address_id'), nullable=False)
    h_pool_id = Column(Integer, ForeignKey('h_pools.h_pool_id'), nullable=False)
