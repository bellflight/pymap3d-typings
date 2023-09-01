from typing import Optional

from pymap3d.ellipsoid import Ellipsoid

def geoc2geod(
    geocentric_lat: float,
    geocentric_distance: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> float: ...
def geodetic2geocentric(
    geodetic_lat: float, alt_m: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def geocentric2geodetic(
    geocentric_lat: float,
    alt_m: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> float: ...
def geodetic2isometric(
    geodetic_lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def isometric2geodetic(
    isometric_lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def conformal2geodetic(
    conformal_lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def geodetic2conformal(
    geodetic_lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def geodetic2rectifying(
    geodetic_lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def rectifying2geodetic(
    rectifying_lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def geodetic2authalic(
    geodetic_lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def authalic2geodetic(
    authalic_lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def geodetic2parametric(
    geodetic_lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
def parametric2geodetic(
    parametric_lat: float, ell: Optional[Ellipsoid] = None, deg: bool = True
) -> float: ...
