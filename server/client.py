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

    def setFile(self):
        """Carregando documento a ser enviado"""
        print('+--------------------------------+')
        print('|      Carregando Documento      |')
        print('+--------------------------------+')
        try:
            self.file = open(self.filePath, 'rb').read() #ainda não estou pegando o arquivo inteiro
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