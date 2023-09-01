import datetime

from nptyping import Float, NDArray, Shape

def eci2ecef(
    x: float, y: float, z: float, time: datetime.datetime
) -> tuple[float, float, float]: ...
def ecef2eci(
    x: float, y: float, z: float, time: datetime.datetime
) -> tuple[float, float, float]: ...
def R3(x: float) -> NDArray[Shape["3, 3"], Float]: ...
