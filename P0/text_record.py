class TextRecord:

    def __init__(self, text):

        self.sending_number: str = text[0]
        self.recieving_number: str = text[1]
        self.timestamp: str = text[2]
