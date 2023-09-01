from typing import Optional

from pymap3d.ellipsoid import Ellipsoid

def vdist(
    Lat1: float,
    Lon1: float,
    Lat2: float,
    Lon2: float,
    ell: Optional[Ellipsoid] = None,
) -> tuple[float, float]: ...
def vreckon(
    Lat1: float,
    Lon1: float,
    Rng: float,
    Azim: float,
    ell: Optional[Ellipsoid] = None,
) -> tuple[float, float]: ...
def track2(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
    ell: Optional[Ellipsoid] = None,
    npts: int = 100,
    deg: bool = True,
) -> tuple[list[float], list[float]]: ...
