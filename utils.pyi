from typing import Optional

from pymap3d.ellipsoid import Ellipsoid

def cart2pol(x: float, y: float) -> tuple[float, float]: ...
def pol2cart(theta: float, rho: float) -> tuple[float, float]: ...
def cart2sph(x: float, y: float, z: float) -> tuple[float, float, float]: ...
def sph2cart(az: float, el: float, r: float) -> tuple[float, float, float]: ...
def sanitize(
    lat: float, ell: Optional[Ellipsoid], deg: bool
) -> tuple[float, Ellipsoid]: ...
