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
from gate import Gate
from message import Message

# Class
class Client(Gate):
    'Classe Client, capaz de enviar dados'

    def __init__(self,name):
        super().__init__(name)
        # super(name, self).__init__()
        #File Path
        self.filePath = r"/home/borg/Documents/graduacao/camadaFisicaDaComputacao/projeto3/camadaFisica-projeto3/client/image.png"
        self.file = b''
        self.packageList = []
        self.widthPayload = 30 #project restriction widthPayload <= 114
        self.message = Message()

        self.packageCounter = 0
        self.totalPackages = 0
        self.packageCounterReceived = 0
        self.totalPackagesReceived = 0
        self.messageReceived = 0
        self.payloadWidth = 0 
        self.check = False

    def setFile(self):
        """Carregando documento a ser enviado"""
        print('+--------------------------------+')
        print('|      Carregando Documento      |')
        print('+--------------------------------+')
        try:
            self.file = open(self.filePath, 'rb').read() 
            print('|      Documento Carregado!      |')
            print('+--------------------------------+')
        except:
            print('|   Falha ao carregar Documento  |')
            print('+--------------------------------+')

    def sliceFile(self):
        """
        Slice files
        """
        #Number of packages

        N = int(len(self.file)/self.widthPayload)
        for k in range(0,N):
            if k == N-1: #whether is the last, we must go until the final, that is, widthPayload
                self.packageList.append(self.file[self.widthPayload*k:len(self.file)])
            else:
                self.packageList.append(self.file[self.widthPayload*k: self.widthPayload*(k+1)])

    def readMessage(self):
        if self.messageReceived == 123: #handshake
            self.message.work()
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

