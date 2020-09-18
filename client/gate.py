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

    def run(self):
        """Run!!"""
        self.openGate()

    def setDataSize(self, head,payload,eop):
        """DataSize is update with the lenght of head, payload and eop expected"""
        self.dataSize = len(head)+len(payload)+len(eop)


    def openGate(self):
        """Open the gate"""
        self.com.enable()

    def closeGate(self):
        """Fechando a porta no sistema"""
        self.com.disable()

    def setMessage(self, message):
        """Inicialização de Conversa. Pode enviar uma string em bytes específica, bem semelhante ao protocolo"""
        self.message = message

    def sendPackage(self,package):
        """send package"""
        self.com.sendData(package)
        print('+--------------------------------+')
        print('|       Pacote Enviado           |')
        print('+--------------------------------+')







