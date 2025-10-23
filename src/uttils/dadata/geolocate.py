from dadata import Dadata
from config_reader import config
from typing import Any

def geoLocate(lat: float, lon: float) -> str:
     with Dadata(config.dadata_token.get_secret_value(), config.dadata_secret.get_secret_value(), timeout=1) as dadata:
          result: list[Any] = dadata.geolocate(name="address", lat=lat, lon=lon)
          return result[0]["value"] if result else "Не определяется {} {}".format(lat, lon)
          