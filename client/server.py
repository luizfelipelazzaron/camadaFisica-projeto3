#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#################################
# Camada Física da Computação
# Luiz Felipe Lazzaron
# 10/09/2020
# Server
#################################

# Time Library
import time

# Enlace 
from gate import Gate
from message import Message

# Class
class Server(Gate):
    'Classe Server, capaz de receber dados'

    def __init__(self,name):
        super().__init__(name)
        #File Path
        self.filePath = r"/home/borg/Documents/graduacao/camadaFisicaDaComputacao/projeto3/camadaFisica-projeto3/client/imageReceived.png"
        self.message = Message()
        self.packageCounter = 0
        self.totalPackages = 9 #número de pacotes
        self.packageCounterReceived = 0
        self.totalPackagesReceived = 0
        self.messageReceived = 0
        self.payloadWidth = 0 
        self.check = False

    def readMessage(self):
        if self.messageReceived == 123: #handshake
            self.message.handshake()
        elif self.messageReceived == 125: #success
            None
        elif self.messageReceived == 144: #failure
            None
        elif self.messageReceived == 808: #bye
            self.message.bye()
        else:
            None

    def receivePackage(self):
        receivedHead, number =  self.com.getData(self.headWidth)
        print('+--------------------------------+')
        print('|       Head Recebido            |')
        print('+--------------------------------+')
        self.setHeadReceived(receivedHead)
        if self.payloadWidth != 0:
            self.payloadReceived, number =  self.com.getData(self.payloadWidth)
        self.eopReceived, number = self.com.getData(self.eopWidth)
        self.checkPackage()
            

    def setHeadReceived(self,head):
        self.packageCounterReceived = self.convertBytesToInt(head[0:2])
        self.totalPackagesReceived = self.convertBytesToInt(head[2:4])
        self.messageReceived = self.convertBytesToInt(head[4:6])
        self.payloadWidth = self.convertBytesToInt(head[6:self.headWidth])


    def checkPackage(self):
        checkPackageNumber = self.packageCounter == self.packageCounterReceived
        print("self.packageCounter{}".format(self.packageCounter))
        print("self.packageCounterReceived{}".format(self.packageCounterReceived))
        checkTotalPackage = self.totalPackages == self.totalPackagesReceived
        checkEop = self.eopCode == self.convertBytesToInt(self.eopReceived)
        if checkEop:
            if checkTotalPackage:
                if checkPackageNumber:
                    print('+--------------------------------+')
                    print('|     Pacote nos Conformes       |')
                    print('+--------------------------------+')
                    self.check = True
                else:
                    print("o número do pacote não bate")
            else:
                print("o número total de pacotes não bate")
        else:
            print("o EOP não bate")



    def convertBytesToInt(self, b):
        'type(b)=bytes, return int'
        return int.from_bytes(b, byteorder='big')