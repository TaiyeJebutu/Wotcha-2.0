import encodings


class Filter:

    def __init__(self):
        ...

    @staticmethod
    def upper_case(message:str):
        return message.upper()

    @staticmethod
    def lower_case(message:str):
        return message.lower()

    @staticmethod
    def bin(message:str):
        return ' '.join(format(x, 'b') for x in bytearray(message, 'utf-8'))
