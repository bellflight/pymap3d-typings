from typing import Optional
from pymap3d.ellipsoid import Ellipsoid

def meridian_dist(
    lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def meridian_arc(
    lat1: float, lat2: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def loxodrome_inverse(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float]: ...
def loxodrome_direct(
    lat1: float,
    lon1: float,
    rng: float,
    a12: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def departure(
    lon1: float,
    lon2: float,
    lat: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> float: ...
def meanm(
    lat: float, lon: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> tuple[float, float, float]: ...
