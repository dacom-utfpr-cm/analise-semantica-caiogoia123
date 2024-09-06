import configparser

class MyError:
    def __init__(self, et):
        self.config = configparser.RawConfigParser()
        self.config.read('ErrorMessages.properties')
        self.errorType = et

    def newError(self, showKey, key, linha=None, coluna=None, **data):
        if showKey:
            return key if linha is None or coluna is None else f"{key}"

        message = f"Erro[{linha}][{coluna}]: " if linha is not None and coluna is not None else ""

        if key:
            message += self.config.get(self.errorType, key)

        if data:
            data_str = ", ".join(f"{k}: {v}" for k, v in data.items())
            message += ", " + data_str if data_str else ""

        return message
