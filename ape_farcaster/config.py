from typing import Any

from ape_farcaster.models import *

FARCASTER_API_BASE_URL = "https://api.warpcast.com/v2/"


class ConfigurationParams(BaseModel):
    username: str | None = None
    password: str | None = None
    base_path: str = FARCASTER_API_BASE_URL
    base_options: dict[Any, Any] | None = None


class Configuration(BaseModel):
    params: ConfigurationParams | None

    def __init__(self, **data: Any):  # pragma: no cover
        super().__init__(**data)
        self.params = ConfigurationParams(**data)
