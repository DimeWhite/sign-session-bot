from dadata import Dadata
from config_reader import config

def geoLocate(lat: float, lon: float) -> str:
     with Dadata(config.dadata_token.get_secret_value(), config.dadata_secret.get_secret_value(), timeout=1) as dadata:
          return dadata.geolocate(name="address", lat=lat, lon=lon)[0]["value"]
          