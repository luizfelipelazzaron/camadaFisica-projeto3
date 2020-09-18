from message import Message
class Package(object):
    'Package class'
    def __init__(self):
        self.package = b''
        self.head = b''
        self.headWidth = 10 #project restriction
        self.payload = b''
        self.payloadWidth = 0
        self.eop = b''
        self.eopCode = 541526 #arbitray eop
        self.eopWidth = 4 #project restriction
        

    def setPackage(self,stage):
        "stage is an int"
        if stage == 0:
            message = Message()
            message.handshake()
            self.setHead(0,0,message.message)
            self.setEop()
        else: 
            None
        print('+--------------------------------+')
        print('|     Preparando o Pacote        |')
        print('+--------------------------------+')

        print("head:{}".format(self.head))
        print("payload:{}".format(self.payload))
        print("eop:{}".format(self.eop))

        self.package = self.head + self.payload + self.eop
        self.payloadWidth = len(self.payload)

    def setHead(self, n, t,message):
        """
        n is the package number ,
        t is the total of packages,
        type(n) = int,
        type(t) = int,
        type(message) = int
        """
        packageNumberWidth = 2
        totalOfPackagesWidth = 2
        messageWidth = 2
        payloadWidth = self.headWidth - (packageNumberWidth + totalOfPackagesWidth + messageWidth)  #packageNumberWidth + totalOfPackagesWidth must be smaller than headWidth
        packageNumber = self.convertIntToBytes(n,packageNumberWidth)
        totalOfPackages = self.convertIntToBytes(t,totalOfPackagesWidth)
        message = self.convertIntToBytes(message,totalOfPackagesWidth)
        payloadWidthBytes = self.convertIntToBytes(self.payloadWidth,payloadWidth)

        self.head = packageNumber +  totalOfPackages + message + payloadWidthBytes #because 


    def setPayload(self,n,packageList):
        """
            n is the package number ,
            packageList is a sliced file,
            type(n) = int
            type(packageList) = list
        """
        self.payload = packageList[n]

    def convertIntToBytes(self,integer,lenght):
        """
        integer is an int ,
        lenght is the number of bytes that you transform the integer.
        Return in bytes
        """
        return (integer).to_bytes(lenght, byteorder='big')

    def setEop(self):
        self.eop = self.convertIntToBytes(self.eopCode, self.eopWidth)