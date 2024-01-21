from typing import Protocol, List, Dict


class BaseSettingProtocol(Protocol):

    URL: str
    TYPE_KEYS: List[str]
    MAP_FRE_KEY: Dict[str, str]


class BaseSetting(BaseSettingProtocol):

    URL = ""
    TYPE_KEYS = []
    MAP_FRE_KEY = {}
