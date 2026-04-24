from enum import Enum

class OddsType(Enum):
    FIXED = "FIXED"
    PROBABILITY = "PROBABILITY"
    AMERICAN = "AMERICAN"
    DECIMAL = "DECIMAL"