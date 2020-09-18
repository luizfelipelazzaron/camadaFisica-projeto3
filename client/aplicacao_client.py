#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação do Client
####################################################
#Acesssing gates by the code: sudo chmod 666 /dev/tnt*

import time
from client import Client
from message import Message
from package import Package
from enlaceRx import RX

serialName = "/dev/tnt1"

def main():
    try:
        client = Client(serialName)
        client.openGate()

        client.setFile()
        
        package = Package()
        package.setPackage(0)

        client.sendPackage(package.package)

        client.com.rx.clearBuffer()

        client.receivePackage()

        # print("client.messageReceived:{}".format(client.messageReceived))


        client.closeGate()

        # message = Message()
        # print("message:{}".format(message.message))
        # message.handshake()
        # print("message:{}".format(message.message))

        # package = Package()
        # package.setEop()
        # package.setHead(1,1,message.message)
        # package.setPackage()
        # print("package.package:{}".format(package.package))
        # print("type of package:{}".format(package.package))
        # print(type(package.package))






        # package = Package()
        # package.setEop()
        # package.setHead(1,1,message.message)
        # package.setPackage()
        # print(package.package)
        # print(type(package.package))


        # client.setFile()
        # client.sliceFile()

        # package = Package()
        # package.setHead(1,12)




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



