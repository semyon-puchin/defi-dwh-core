from enum import Enum


class RevenueType(Enum):
    LENDING: str = 'LENDING'
    INCENTIVES: str = 'INCENTIVES'
    TRADING: str = 'TRADING'
    STAKING: str = 'STAKING'
