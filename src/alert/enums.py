from enum import Enum


class LocationTypeEnum(str, Enum):
    oblast = "oblast"
    raion = "raion"
    city = "city"
    hromada = "hromada"
    unknown = "unknown"


class AlertTypeEnum(str, Enum):
    air_raid = "air_raid"
    artillery_shelling = "artillery_shelling"
    urban_fights = "urban_fights"
    chemical = "chemical"
    nuclear = "nuclear"


class AlertStatusResponseEnum(str, Enum):
    A = "A"
    P = "P"
    N = "N"
