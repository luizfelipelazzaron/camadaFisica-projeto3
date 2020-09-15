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

packageNumber = 3 #arbitrary

def main():
    try:
        client = Client('COM1')
        client.setFile()
        client.sliceFile(packageNumber)

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



