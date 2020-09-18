class Message(object):
    'Message class'
    def __init__(self):
        self.message = 0

    def handshake(self):
        'initialize conversation'
        handshakeCode = 123
        self.message = handshakeCode


    def success(self):
        'success message'
        successCode = 125
        self.message = successCode

    def failure(self):
        'failure message'
        failureCode = 144
        self.message = failureCode

    def bye(self):
        'terminate conversation'
        byeCode = 808
        self.message = byeCode

    def work(self):
        """when we work, we don't talk"""
        workCode = 999
        self.message = workCode


