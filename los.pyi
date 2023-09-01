from typing import Optional
from pymap3d.ellipsoid import Ellipsoid

def lookAtSpheroid(
    lat0: float,
    lon0: float,
    h0: float,
    az: float,
    tilt: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
