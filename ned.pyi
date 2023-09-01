from pymap3d.ellipsoid import Ellipsoid
from typing import Optional

def aer2ned(
    az: float, elev: float, slantRange: float, deg: bool = True
) -> tuple[float, float, float]: ...
def ned2aer(
    n: float, e: float, d: float, deg: bool = True
) -> tuple[float, float, float]: ...
def ned2geodetic(
    n: float,
    e: float,
    d: float,
    lat0: float,
    lon0: float,
    h0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def ned2ecef(
    n: float,
    e: float,
    d: float,
    lat0: float,
    lon0: float,
    h0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def ecef2ned(
    x: float,
    y: float,
    z: float,
    lat0: float,
    lon0: float,
    h0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def geodetic2ned(
    lat: float,
    lon: float,
    h: float,
    lat0: float,
    lon0: float,
    h0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def ecef2nedv(
    x: float, y: float, z: float, lat0: float, lon0: float, deg: bool = True
) -> tuple[float, float, float]: ...
