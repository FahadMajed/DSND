class CallRecord:

    def __init__(self, call):

        self.sending_number = call[0]
        self.recieving_number = call[1]
        self.timestamp = call[2]
        self.duration = call[3]