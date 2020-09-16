class Message(object):
    'Message class'
    def __init__(self):
        self.message = 0

    def handshake(self):
        'initialize conversation'
        handshakeCode = 12312
        self.message = handshakeCode

    def success(self):
        'success message'
        successCode = 12541
        self.message = successCode

    def failure(self):
        'failure message'
        failureCode = 14436
        self.message = failureCode

    def bye(self):
        'terminate conversation'
        byeCode = 80890
        self.message = byeCode