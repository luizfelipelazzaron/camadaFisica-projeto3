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

# Class
class Gate(object):
    'Classe Gate. Classe pai de Server e Client'

    def __init__(self, name):
        # Gate Name
        self.name= name 
        self.com = enlace(self.name)
        self.message = ""
        self.packageCounter = 0

    def run(self):
        """Run!!"""
        self.openGate()

    def openGate(self):
        """Open the gate"""
        self.com.enable()
        print('+--------------------------------+')
        print('|         Porta iniciada         |')
        print('+--------------------------------+')
        print('Nome da Porta:{}'.format(self.com.fisica.name))

    def closeGate(self):
        """Fechando a porta no sistema"""
        print("tentando fechar a porta")
        self.com.disable()
        print('+--------------------------------+')
        print('|         Porta fechada          |')
        print('+--------------------------------+')
    
    def setMessage(self, message):
        """Inicialização de Conversa. Pode enviar uma string em bytes específica, bem semelhante ao protocolo"""
        self.message = message

    def sendMessage(self):
        """send message"""
        preparedMessage = self.prepareMessage()
        self.com.sendData(preparedMessage)
        print('+--------------------------------+')
        print('|       Mensagem Enviada         |')
        print('+--------------------------------+')

    # def prepareMessage(self):
    #     """prepare message"""
    #     convertMessage = ""
    #     if type(self.message) == str:
    #         convertMessage = self.convertStringToBytes(self.message)
    #     return convertMessage

    # def convertStringToBytes(self,value):
    #     """value is in string. Return in bytes"""
    #     return str.encode(value)

    # def convertBytesToString(self,value):
    #     """value is in bytes. Return in string"""
    #     return value.decode()






