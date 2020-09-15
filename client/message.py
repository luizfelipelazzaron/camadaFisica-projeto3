class Message(object):
    'Message class'
    def __init__(self):
        self.message = b''
    def handshake(self):
        self.message = b'handshake'
    def success(self):
        self.message = b'success'
    def failure(self):
        self.message = b'failure'
    def bye(self):
        self.message = b'bye'