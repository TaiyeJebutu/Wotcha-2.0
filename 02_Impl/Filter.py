


class Filter:

    def __init__(self):
        ...

    def filter(self,message,decoder = 'bin'):
        if decoder == "upper":
            return Filter.upper_case(message)
        if decoder == "lower":
            return Filter.lower_case(message)
        if decoder == "bin":
            return Filter.bin(message)
        if decoder == "reverse":
            return Filter.reverse(message)

    @staticmethod
    def upper_case(message:str):
        return message.upper()

    @staticmethod
    def lower_case(message:str):
        return message.lower()

    @staticmethod
    def bin(message:str):
        return ' '.join(format(x, 'b') for x in bytearray(message, 'utf-8'))

    @staticmethod
    def reverse(message:str):
        return ' '.join(map(lambda s:s[::-1], message.split()))
