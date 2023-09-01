from typing import Optional
from pymap3d.ellipsoid import Ellipsoid

def enu2aer(
    e: float, n: float, u: float, deg: bool = True
) -> tuple[float, float, float]: ...
def aer2enu(
    az: float, el: float, srange: float, deg: bool = True
) -> tuple[float, float, float]: ...
def enu2geodetic(
    e: float,
    n: float,
    u: float,
    lat0: float,
    lon0: float,
    h0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def geodetic2enu(
    lat: float,
    lon: float,
    h: float,
    lat0: float,
    lon0: float,
    h0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
