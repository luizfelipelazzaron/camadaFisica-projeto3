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
        counter = 0
        state = 'handshake'
        while state == "handshake":
            server = Server(serialName)
            server.openGate()
            print('+--------------------------------+')
            print('|         Porta iniciada         |')
            print('+--------------------------------+')
            server.receivePackage()
            if server.check:
                counter=1
                package = Package()
                package.setPackage(0,0,9)
                server.sendPackage(package.package)
                server.closeGate()
                state = 'receivePackages'

        lista = []
        while state == "receivePackages":
            server = Server(serialName)
            server.packageCounter = counter
            server.openGate()
            server.receivePackage()
            if server.check and counter < 9:
                lista.append(server.payloadReceived)
                package = Package()
                package.setPackage(2,counter,9)
                print("contador: {}".format(counter))
                server.sendPackage(package.package)
                server.closeGate()
                counter += 1
            elif server.check:
                lista.append(server.payloadReceived)
                package = Package()
                package.setPackage(2,counter,9)
                server.sendPackage(package.package)
                server.closeGate()
                break
            print(lista)


        server = Server(serialName)
        server.openGate()
        print('+---------------------------------+')
        print('| esperando mensagem de conclusão |')
        print('+---------------------------------+')
        server.receivePackage()
        server.closeGate()


        print('+--------------------------------+')
        print('|         Porta fechada          |')
        print('+--------------------------------+')

    except Exception as e:
        print("Um erro aconteceu:")
        print('Failed to upload to ftp: '+str(e))
if __name__ == "__main__":
    main()



