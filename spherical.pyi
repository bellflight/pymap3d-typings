from typing import Optional
from pymap3d.ellipsoid import Ellipsoid

def geodetic2spherical(
    lat: float,
    lon: float,
    alt: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def spherical2geodetic(
    lat: float,
    lon: float,
    radius: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
