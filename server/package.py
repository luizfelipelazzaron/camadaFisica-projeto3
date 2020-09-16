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

    def setPackage(self):
        self.package = self.head + self.payload + self.eop
        self.payloadWidth = len(self.package)

    def setHead(self, n, t):
        """
        n is the package number ,
        t is the total of packages,
        type(n) = int,
        type(t) = int
        """
        packageNumberWidth = 2
        totalOfPackagesWidth = 4
         #packageNumberWidth + totalOfPackagesWidth must be smaller than headWidth
        packageNumber = self.convertIntToBytes(n,packageNumberWidth)
        totalOfPackages = self.convertIntToBytes(t,totalOfPackagesWidth)
        payloadWidth = self.convertIntToBytes(self.payloadWidth,self.headWidth - totalOfPackagesWidth - packageNumberWidth)

        self.head = packageNumber +  totalOfPackages + payloadWidth #because len(self.head) == 10 is a project restriction

    def setPayload(self,n,packageList):
        """
            n is the package number ,
            packageList is a sliced file,
            type(n) = int
            type(packageList) = list
        """
        self.payload = packageList[n]

    def setPayloadMessage(self,message):
        """type(message)=bytes"""
        self.payload = message

    def convertIntToBytes(self,integer,lenght):
        """
        integer is an int ,
        lenght is the number of bytes that you transform the integer.
        Return in bytes
        """
        return (integer).to_bytes(lenght, byteorder='big')

    def setEop(self):
        self.eop = self.convertIntToBytes(self.eopCode, self.eopWidth)