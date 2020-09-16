#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação do Client
####################################################
import time
from client import Client
from message import Message
from package import Package

serialName = "/dev/tnt1"

def main():
    try:
        client = Client(serialName)
        client.openGate()

        message = Message()
        message.handshake()

        package = Package()
        package.setEop()
        package.setPayloadMessage(message.message)
        package.setHead(1,1)
        package.setPackage()
        client.setMessage(package.package)
        client.sendMessage()

        # client.setFile()
        # client.sliceFile()

        # package = Package()
        # package.setHead(1,12)

        # message = Message()
        # message.handshake()


        # client = Client('COM1')
        # client.run()
        # client.setMessage("handshake")
        # client.sendMessage()
        # client.closeGate()
    except Exception as e:
        print("Um erro aconteceu:")
        print('Failed to upload to ftp: '+str(e))
if __name__ == "__main__":
    main()



