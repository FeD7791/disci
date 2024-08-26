from typing import NamedTuple
import pandas as pd

class coordinates(NamedTuple):
    city: str
    lat: float
    lon: float

#Probar correr mypy con las distintas lineas, en la segunda obtendremos error
argentina = coordinates('BsAs', 37.12, -23.67)
# argentina = coordinates(50, 37.12, -23.67)

print(argentina)