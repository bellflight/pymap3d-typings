from typing import Optional, Literal
from pymap3d.ellipsoid import Ellipsoid

def eqavol(ell: Optional[Ellipsoid] = None) -> float: ...
def authalic(ell: Optional[Ellipsoid] = None) -> float: ...
def rectifying(ell: Optional[Ellipsoid] = None) -> float: ...
def euler(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> float: ...
def curve(
    lat: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
    method: Literal["mean", "norm"] = "mean",
) -> float: ...
def triaxial(
    ell: Optional[Ellipsoid] = None, method: Literal["mean", "norm"] = "mean"
) -> float: ...
def biaxial(
    ell: Optional[Ellipsoid] = None, method: Literal["mean", "norm"] = "mean"
) -> float: ...
