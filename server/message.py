class Message(object):
    'Message class'
    def __init__(self):
        self.message = b''
        self.messageWidth = 0
    def setMessageWidth(self):
        'set message width'
        self.messageWidth = len(self.message)
    def handshake(self):
        'initialize conversation'
        self.message = b'handshake'
        self.setMessageWidth()
    def success(self):
        'success message'
        self.message = b'success'
        self.setMessageWidth()
    def failure(self):
        'failure message'
        self.message = b'failure'
        self.setMessageWidth()
    def bye(self):
        'terminate conversation'
        self.message = b'bye'
        self.setMessageWidth()