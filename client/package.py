class Package(object):
    'Package class'
    def __init__(self):
        self.head = b''
        self.payload = b''
        self.eop = b''
        self.package = b''

    def setHead(self, n, t):
        """
        n is the package number ,
        t is the total of packages,
        type(n) = int,
        type(t) = int
        """
        self.head = self.convertIntToBytes(n,2) + self.convertIntToBytes(t,2)  #because len(self.head) == 4 is a project restriction

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