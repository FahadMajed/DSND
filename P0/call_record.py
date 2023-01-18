class CallRecord:

    def __init__(self, call):

        self.sending_number: str = call[0]
        self.recieving_number: str = call[1]
        self.timestamp: str = call[2]
        self.duration: str = call[3]
