#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação do Client
####################################################
#Acesssing gates by the code: sudo chmod 666 /dev/tnt*

import time
from server import Server
from message import Message
from package import Package

serialName = "/dev/tnt0"

def main():
    try:
        server = Server(serialName)
        server.openGate()

        #Handshake
        server.receivePackage()
        if server.check:
            package = Package()
            package.setPackage(0)
            server.sendPackage(package.package)



        server.closeGate()

    except Exception as e:
        print("Um erro aconteceu:")
        print('Failed to upload to ftp: '+str(e))
if __name__ == "__main__":
    main()



