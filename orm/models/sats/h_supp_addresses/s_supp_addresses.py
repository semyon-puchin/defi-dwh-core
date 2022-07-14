from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean

from orm.models.main import Base


class SatelliteSupportAddresses(Base):

    __tablename__ = 's_supp_addresses'

    s_supp_address_id = Column(Integer, primary_key=True)  # PK
    h_supp_address_id = Column(Integer, ForeignKey('h_supp_addresses.h_supp_address_id'), nullable=False)
    s_supp_address_pid = Column(Integer, nullable=False)
