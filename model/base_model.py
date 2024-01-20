from typing import Protocol, Union, List
from common.exception import ModelColumnNotFoundError, ModelColumnKeyNotInit, ModelColumnKeyInitNoEqual


class ModelProtocol(Protocol):

    def __init__(self, *args, **kwargs) -> None:
        self._data = {}

    def get_dict_info(self) -> dict:
        """
        :return: a dict abount model info
        """
        return dict()

    def get_columns_name(self) -> List[Union[str, int]]:
        """
        :return: a list contains all columns name, what meaned reflect to [*]setting
        """
        return []

    def _column_keys(self) -> List[str]:
        """
        :return: a list model contains init params, subclass must rewrite
        """
        return []

    def parse_to_text(self) -> str:
        return ""


class BaseModel(ModelProtocol):

    def __getattr__(self, item):
        if item in self._data:
            return self._data[item]
        raise ModelColumnNotFoundError("%s has not found column named %s" % item)

    def __init__(self, **kwargs):
        self._data = {}
        self.check_type_keys(kwargs)
        self._data.update(kwargs)

    def get_dict_info(self) -> dict:
        return self._data

    def get_columns_name(self) -> [Union[str, int]]:
        return [k for k in self._data]

    def _column_keys(self) -> List[str]:
        return []

    def check_type_keys(self, kwargs: dict) -> None:
        column_keys = self._column_keys()
        for key in column_keys:
            if key not in column_keys:
                raise ModelColumnKeyNotInit("%s key not exclude in init param" % key)
        if len(kwargs) != len(column_keys):
            raise ModelColumnKeyInitNoEqual("init param lens not equal to pointed param")






