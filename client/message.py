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
        self.message = self.convertStringToBytes('handshake')
        print("message:{}".format(self.message))
        print("type message:{}".format(type(self.message)))
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

    def convertStringToBytes(self,value):
        # b = bytearray(value,'utf-8')
        message = "lalala"
        b = [element.encode("hex") for element in message]
        print(b)
        return b