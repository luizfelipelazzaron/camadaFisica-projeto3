#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#################################
# Camada Física da Computação
# Luiz Felipe Lazzaron
# 10/09/2020
# Client
#################################

# Time Library
import time

# Enlace 
from enlace import enlace
from package import Package
from message import Message

# Class
class Gate(object):
    'Classe Gate. Classe pai de Server e Client'

    def __init__(self, name):
        # Gate Name
        self.name= name 
        self.com = enlace(self.name)
        self.packageReceived = b''
        self.payloadReceived = b''
        self.eopReceived = b''
        self.eopCode = 541526 #arbitray eop
        self.headWidth = 10 #project restriction
        self.eopWidth = 4 #project restriction
        # self.packageCounter = 0
        # self.totalPackages = 0
        # self.packageCounterReceived = 0
        # self.totalPackagesReceived = 0
        # self.messageReceived = 0
        # self.payloadWidth = 0 
        # self.check = False

    def run(self):
        """Run!!"""
        self.openGate()

    def setDataSize(self, head,payload,eop):
        """DataSize is update with the lenght of head, payload and eop expected"""
        self.dataSize = len(head)+len(payload)+len(eop)


    def openGate(self):
        """Open the gate"""
        self.com.enable()
        print('+--------------------------------+')
        print('|         Porta iniciada         |')
        print('+--------------------------------+')
        print('Nome da Porta:{}'.format(self.com.fisica.name))

    def closeGate(self):
        """Fechando a porta no sistema"""
        self.com.disable()
        print('+--------------------------------+')
        print('|         Porta fechada          |')
        print('+--------------------------------+')

    def setMessage(self, message):
        """Inicialização de Conversa. Pode enviar uma string em bytes específica, bem semelhante ao protocolo"""
        self.message = message

    def sendPackage(self,package):
        """send package"""
        self.com.sendData(package)
        print('+--------------------------------+')
        print('|       Pacote Enviado           |')
        print('+--------------------------------+')

    def setHead(self,head):
        self.packageCounterReceived = self.convertBytesToInt(head[0:2])
        self.totalPackagesReceived = self.convertBytesToInt(head[2:4])
        self.messageReceived = self.convertBytesToInt(head[4:6])
        self.payloadWidth = self.convertBytesToInt(head[6:self.headWidth])

    # def receivePackage(self):
    #     time_start = time.time()
    #     delta_t = 0
    #     print("getIsEmpty:{}".format(self.com.rx.getIsEmpty()))
    #     while self.com.rx.getIsEmpty() and delta_t <5:
    #         time.sleep(1)
    #         time_end = time.time()
    #         delta_t = time_end - time_start
    #         print("{}...".format(int(delta_t)))
    #     if delta_t > 5 and self.com.rx.getIsEmpty():
    #         print("não chegou meu velho")
    #     else:
    #         receivedHead, number =  self.com.getData(self.headWidth)
    #         print('+--------------------------------+')
    #         print('|       Head Recebido            |')
    #         print('+--------------------------------+')
    #         self.setHead(receivedHead)
    #         if self.payloadWidth != 0:
    #             self.payloadReceived, number =  self.com.getData(self.payloadWidth)
    #         self.eopReceived, number = self.com.getData(self.eopWidth)
    #         self.checkPackage()
            

    # def checkPackage(self):
    #     if self.packageCounter != 0:
    #         None
    #     else:
    #         checkPackageNumber = self.packageCounter == self.packageCounterReceived
    #         checkTotalPackage = self.totalPackages == self.totalPackagesReceived
    #         checkEop = self.eopCode == self.convertBytesToInt(self.eopReceived)
    #     if checkEop:
    #         if checkTotalPackage:
    #             if checkPackageNumber:
    #                 print('+--------------------------------+')
    #                 print('|     Pacote nos Conformes       |')
    #                 print('+--------------------------------+')
    #                 self.check = True
    #             else:
    #                 print("o número do pacote não bate")
    #         else:
    #             print("o número total de pacotes não bate")
    #     else:
    #         print("o EOP não bate")



    # def convertBytesToInt(self, b):
    #     'type(b)=bytes, return int'
    #     return int.from_bytes(b, byteorder='big')

    # # def convertBytesToString(self,value):
    # #     """value is in bytes. Return in string"""
    # #     return value.decode()






