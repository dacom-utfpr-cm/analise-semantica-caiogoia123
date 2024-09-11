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
            # Obtém a mensagem do arquivo de propriedades
            message_template = self.config.get(self.errorType, key)

            # Substitui os placeholders '{}' pelos valores no dicionário `data`
            if data:
            # Converte os valores em uma lista e conta o número total de itens
                num_items = sum(len(v) if isinstance(v, list) else 1 for v in data.values())
                # print(f"Total de itens dentro de data.values(): {num_items}")

                if num_items == 1:
                    message = message_template.format(*data.values())
                else:
                    # print(len(*data.values()))
                    # print(*data.values())
                    dataAux = data['data']
                    message = message_template.format(*dataAux)
            else:
                return message_template
        return message
