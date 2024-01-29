from enum import Enum

try:
    from typing import Literal, Union
except ImportError:
    from typing_extensions import Literal
from typing import Optional


class LocationHint(Enum):
    USA = {
        "locale": "en-US",
        "LocationHint": [
            {
                "country": "United States",
                "state": "California",
                "city": "Los Angeles",
                "timezoneoffset": 8,
                "countryConfidence": 8,
                "Center": {
                    "Latitude": 34.0536909,
                    "Longitude": -118.242766,
                },
                "RegionType": 2,
                "SourceType": 1,
            },
        ],
    }
    CHINA = {
        "locale": "zh-CN",
        "LocationHint": [
            {
                "country": "China",
                "state": "",
                "city": "Beijing",
                "timezoneoffset": 8,
                "countryConfidence": 8,
                "Center": {
                    "Latitude": 39.9042,
                    "Longitude": 116.4074,
                },
                "RegionType": 2,
                "SourceType": 1,
            },
        ],
    }
    EU = {
        "locale": "en-IE",
        "LocationHint": [
            {
                "country": "Ireland",
                "state": "",
                "city": "Dublin",
                "timezoneoffset": 1,
                "countryConfidence": 8,
                "Center": {
                    "Latitude": 53.2732,
                    "Longitude": -6.2109,
                },
                "RegionType": 2,
                "SourceType": 1,
            },
        ],
    }
    UK = {
        "locale": "en-GB",
        "LocationHint": [
            {
                "country": "United Kingdom",
                "state": "",
                "city": "London",
                "timezoneoffset": 0,
                "countryConfidence": 8,
                "Center": {
                    "Latitude": 51.5074,
                    "Longitude": -0.1278,
                },
                "RegionType": 2,
                "SourceType": 1,
            },
        ],
    }


LOCATION_HINT_TYPES = Optional[Union[LocationHint, Literal["USA", "CHINA", "EU", "UK"]]]
