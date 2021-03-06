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
        self.totalPackages = 9 #número de pacotes
        self.packageCounterReceived = 0
        self.totalPackagesReceived = 0
        self.messageReceived = 0
        self.payloadWidth = 0 
        self.check = False
        self.connection = False

    def setFile(self):
        """Carregando documento a ser enviado"""
        try:
            self.file = open(self.filePath, 'rb').read() 
        except:
            print('+--------------------------------+')
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
            print('+-------------------------------------------+')
            print("|  Servidor inativo. Tentar novamente? S/N  |")
            print('+-------------------------------------------+')
        else:
            receivedHead, number =  self.com.getData(self.headWidth)
            print('+--------------------------------+')
            print('|       Head Recebido            |')
            print('+--------------------------------+')
            self.setHeadReceived(receivedHead)
            if self.payloadWidth != 0:
                self.payloadReceived, number =  self.com.getData(self.payloadWidth)
            self.eopReceived, number = self.com.getData(self.eopWidth)
            self.checkPackage()
            self.connection = True



    def receiveMessage(self,n):
        self.packageCounter = n
        print("getIsEmpty:{}".format(self.com.rx.getIsEmpty()))
        while self.com.rx.getIsEmpty():
            print("esperando resposta..")
            time.sleep(1)
        else:
            print("Resposta Recebida..")
            self.packageCounter = n
            receivedHead, number =  self.com.getData(self.headWidth)
            self.setHeadReceived(receivedHead)
            print("mensagem recebida: {}".format(self.messageReceived))
            if self.payloadWidth != 0:
                self.payloadReceived, number =  self.com.getData(self.payloadWidth)
            self.eopReceived, number = self.com.getData(self.eopWidth)



    def setHeadReceived(self,head):
        self.packageCounterReceived = self.convertBytesToInt(head[0:2])
        self.totalPackagesReceived = self.convertBytesToInt(head[2:4])
        self.messageReceived = self.convertBytesToInt(head[4:6])
        self.payloadWidth = self.convertBytesToInt(head[6:self.headWidth])

    def checkPackage(self):
        if self.packageCounter != 0:
            None
        else:
            print("self.packageCounter{}".format(self.packageCounter))
            print("self.packageCounterReceived{}".format(self.packageCounterReceived))
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

