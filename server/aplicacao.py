#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação do Client
####################################################
import time
from message import Message
from package import Package
from gate import Gate

serialName = "/dev/tnt0"

def main():
    try:
        server = Gate(serialName)
        message = Message()
        message.handshake()
        server.receiveMessage(4)

    except Exception as e:
        print("Um erro aconteceu:")
        print('Failed to upload to ftp: '+str(e))
if __name__ == "__main__":
    main()



