from typing import Optional
import datetime

from pymap3d.ellipsoid import Ellipsoid

def geodetic2ecef(
    lat: float,
    lon: float,
    alt: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def ecef2geodetic(
    x: float,
    y: float,
    z: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def ecef2enuv(
    u: float, v: float, w: float, lat0: float, lon0: float, deg: bool = True
) -> tuple[float, float, float]: ...
def ecef2enu(
    x: float,
    y: float,
    z: float,
    lat0: float,
    lon0: float,
    h0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def enu2uvw(
    east: float,
    north: float,
    up: float,
    lat0: float,
    lon0: float,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def uvw2enu(
    u: float, v: float, w: float, lat0: float, lon0: float, deg: bool = True
) -> tuple[float, float, float]: ...
def eci2geodetic(
    x: float,
    y: float,
    z: float,
    t: datetime.datetime,
    ell: Optional[Ellipsoid] = None,
    *,
    deg: bool = True
) -> tuple[float, float, float]: ...
def geodetic2eci(
    lat: float,
    lon: float,
    alt: float,
    t: datetime.datetime,
    ell: Optional[Ellipsoid] = None,
    *,
    deg: bool = True
) -> tuple[float, float, float]: ...
def enu2ecef(
    e1: float,
    n1: float,
    u1: float,
    lat0: float,
    lon0: float,
    h0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
