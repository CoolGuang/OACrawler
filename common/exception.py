

class OABaseException(Exception):
    pass


class ModelColumnNotFoundError(OABaseException):

    def __init__(self, msg:str, code=-1) -> None:
        super(ModelColumnNotFoundError, self).__init__(msg)
        self.code = code

    def get_code(self):
        return self.code


class ModelColumnKeyNotInit(OABaseException):

    def __init__(self, msg:str, code=-1) -> None:
        super(ModelColumnKeyNotInit, self).__init__(msg)
        self.code = code

    def get_code(self):
        return self.code


class ModelColumnKeyInitNoEqual(OABaseException):

    def __init__(self, msg:str, code=-1) -> None:
        super(ModelColumnKeyInitNoEqual, self).__init__(msg)
        self.code = code

    def get_code(self):
        return self.code


class CrawlerParamTypeError(OABaseException):
    def __init__(self, msg:str, code=-1) -> None:
        super(CrawlerParamTypeError, self).__init__(msg)
        self.code = code

    def get_code(self):
        return self.code

