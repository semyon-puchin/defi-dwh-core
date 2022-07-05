from sqlalchemy import Column, Integer, Text, ForeignKey, Enum

from orm.consts.additional_address_type import AdditionalAddressType
from orm.models.main import Base


class SatelliteAdditionalAddresses(Base):

    __tablename__ = 's_additional_addresses'

    s_address_id = Column(Integer, primary_key=True)
    h_address_id = Column(Integer, ForeignKey('h_addresses.h_address_id'), nullable=False)
    # ---
    s_additional_address = Column(Text, unique=True, nullable=False)
    s_additional_address_type = Column(Enum(AdditionalAddressType), nullable=False)
