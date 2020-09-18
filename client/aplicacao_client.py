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
        choice = 'S'
        while choice =='S':
            client = Client(serialName)
            client.openGate()
            print('+--------------------------------+')
            print('|         Porta iniciada         |')
            print('+--------------------------------+')
            package = Package()
            package.setPackage(0,0,9)
            client.sendPackage(package.package)
            client.com.rx.clearBuffer()
            client.receivePackage()
            client.closeGate()
            if client.connection:
                choice = 'connection'
            else:
                choice = input()

        while choice == "connection":
            for n in range(1,10):#pois são 9 pacotes
                    print("pacote a ser enviado: {}".format(n))
                    client = Client(serialName)
                    client.openGate()
                    client.setFile()
                    client.sliceFile()
                    package = Package()
                    package.setPackagePayload(client.packageList,n,9) #pois são 9 pacotes
                    client.sendPackage(package.package)
                    client.com.rx.clearBuffer()
                    client.receiveMessage()
                    client.closeGate()
            break

        client = Client(serialName)
        client.openGate()
        package = Package()
        package.setPackage(4,0,9)
        client.sendPackage(package.package)
        client.closeGate()

        print('+--------------------------------+')
        print('|         Encerramento           |')
        print('+--------------------------------+')



    except Exception as e:
        print("Um erro aconteceu:")
        print('Failed to upload to ftp: '+str(e))
if __name__ == "__main__":
    main()



