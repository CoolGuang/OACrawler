from typing import Protocol, List, Dict


class BaseSettingProtocol(Protocol):

    URL: Dict[str, str]
    TYPE_KEYS: List[str]
    MAP_FRE_KEY: Dict[str, str]

