from pydantic import BaseModel
from typing import Optional

class GeoInfo(BaseModel):
    city: Optional[str] = None
    country: Optional[str] =  None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    time_zone: Optional[str] =  None

class GeoIPResponse(BaseModel):
    api_version: str
    ip: str
    geo: GeoInfo
    time: int
