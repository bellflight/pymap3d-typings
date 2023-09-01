import datetime
from pymap3d.ellipsoid import Ellipsoid
from typing import Optional

def ecef2aer(
    x: float,
    y: float,
    z: float,
    lat0: float,
    lon0: float,
    h0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def geodetic2aer(
    lat: float,
    lon: float,
    h: float,
    lat0: float,
    lon0: float,
    h0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def aer2geodetic(
    az: float,
    el: float,
    srange: float,
    lat0: float,
    lon0: float,
    h0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def eci2aer(
    x: float,
    y: float,
    z: float,
    lat0: float,
    lon0: float,
    h0: float,
    t: datetime.datetime,
    *,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def aer2eci(
    az: float,
    el: float,
    srange: float,
    lat0: float,
    lon0: float,
    h0: float,
    t: datetime.datetime,
    ell: Optional[Ellipsoid] = None,
    *,
    deg: bool = True,
) -> tuple[float, float, float]: ...
def aer2ecef(
    az: float,
    el: float,
    srange: float,
    lat0: float,
    lon0: float,
    alt0: float,
    ell: Optional[Ellipsoid] = None,
    deg: bool = True,
) -> tuple[float, float, float]: ...
