from typing import Optional
from pymap3d.ellipsoid import Ellipsoid

def geocentric_radius(
    geodetic_lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def parallel(
    lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def meridian(
    lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def transverse(
    lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
