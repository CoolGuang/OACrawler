import copy
import datetime
import json
from typing import Protocol, Union, List, Any
from common.exception import ModelColumnNotFoundError, ModelColumnKeyNotInit, ModelColumnKeyInitNoEqual
from setting.base_setting import BaseSetting


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

    SETTING = BaseSetting

    def __getattr__(self, item):
        if item in self._data:
            return self._data[item]
        raise ModelColumnNotFoundError("%s has not found column named %s" % (self.__class__.__name__,item))

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
        for key in kwargs:
            if key not in column_keys:
                raise ModelColumnKeyNotInit("%s key not exclude in init param" % key)
        if len(kwargs) != len(column_keys):
            raise ModelColumnKeyInitNoEqual("init param lens not equal to pointed param")

    def ch_2_s(self, c) -> Any:
        """
        change c to str
        :return: any
        """
        if isinstance(c, list):
            c = json.dumps([self.ch_2_s(_c) for _c in c])
        elif isinstance(c, dict):
            c = json.dumps({self.ch_2_s(k): self.ch_2_s(v) for k, v in c.items()})
        elif isinstance(c, int) or isinstance(c, float):
            c = str(c)
        elif isinstance(c, datetime.datetime):
            c = c.strftime("%Y-%m-%dT%H:%M:%S")
        else:
            raise TypeError("not exclude type %s" % type(c))
        return c

    def parse_to_text(self) -> str:
        result_str = ""
        for column, value in self._data.items():
            _value = copy.deepcopy(value)
            _column = copy.deepcopy(column)

            _column = self.SETTING.MAP_FRE_KEY[_column]
            _value = self.ch_2_s(_value)
            result_str += _column + ": " + _value + "\n"

        return result_str






