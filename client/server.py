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
        self.file = r"C:\Users\User\Documents\graduacao\4Semestre\CamadaFIsicaDaComputacao\Projetos\projeto3\server\imageReceived.png"
        self.message = Message()
        
        self.packageCounter = 0
        self.totalPackages = 0
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
        time_start = time.time()
        delta_t = 0
        print("getIsEmpty:{}".format(self.com.rx.getIsEmpty()))
        while self.com.rx.getIsEmpty() and delta_t <5:
            time.sleep(1)
            time_end = time.time()
            delta_t = time_end - time_start
            print("{}...".format(int(delta_t)))
        if delta_t > 5 and self.com.rx.getIsEmpty():
            print("não chegou meu velho")
        else:
            receivedHead, number =  self.com.getData(self.headWidth)
            print('+--------------------------------+')
            print('|       Head Recebido            |')
            print('+--------------------------------+')
            self.setHead(receivedHead)
            if self.payloadWidth != 0:
                self.payloadReceived, number =  self.com.getData(self.payloadWidth)
            self.eopReceived, number = self.com.getData(self.eopWidth)
            self.checkPackage()
            

    def checkPackage(self):
        if self.packageCounter != 0:
            None
        else:
            checkPackageNumber = self.packageCounter == self.packageCounterReceived
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