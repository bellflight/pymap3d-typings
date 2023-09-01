import datetime

def azel2radec(
    az_deg: float,
    el_deg: float,
    lat_deg: float,
    lon_deg: float,
    time: datetime.datetime,
) -> tuple[float, float]: ...
def radec2azel(
    ra_deg: float,
    dec_deg: float,
    lat_deg: float,
    lon_deg: float,
    time: datetime.datetime,
) -> tuple[float, float]: ...
