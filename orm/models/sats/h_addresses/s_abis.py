from sqlalchemy import Column, Integer, Text, ForeignKey, Enum

from orm.consts.abi_type import AbiType
from orm.models.main import Base


class SatelliteAbis(Base):

    __tablename__ = 's_abis'

    s_abi_id = Column(Integer, primary_key=True)
    h_address_id = Column(Integer, ForeignKey('h_addresses.h_address_id'), nullable=False)
    # ---
    s_abi_list = Column(Text, unique=True, nullable=False)
    s_abi_type = Column(Enum(AbiType), nullable=False)
