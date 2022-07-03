from enum import Enum


class ProtocolType(Enum):
    LENDING: str = 'LENDING'
    DERIVATIVES: str = 'DERIVATIVES'
    STAKING: str = 'STAKING'
    SYNTHS: str = 'SYNTHS'
    ASSET_MANAGER: str = 'ASSET_MANAGER'
    DEX: str = 'DEX'
    ASSET_MANAGEMENT: str = 'ASSET_MANAGEMENT'
