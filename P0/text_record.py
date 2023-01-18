class TextRecord:

    def __init__(self, text):

        self.sending_number = text[0]
        self.recieving_number = text[1]
        self.timestamp = text[2]