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
        #File Path
        self.filePath = r"C:\Users\User\Documents\graduacao\4Semestre\CamadaFIsicaDaComputacao\Projetos\projeto3\client\image.png"
        self.file = b''
        self.packageList = []
        self.widthPayload = 114 #project restriction

    def setFile(self):
        """Carregando documento a ser enviado"""
        print('+--------------------------------+')
        print('|      Carregando Documento      |')
        print('+--------------------------------+')
        try:
            self.file = open(self.filePath, 'rb').read(self.widthPayload) #ainda não estou pegando o arquivo inteiro
            print('|      Documento Carregado!      |')
            print('+--------------------------------+')
        except:
            print('|   Falha ao carregar Documento  |')
            print('+--------------------------------+')

    def sliceFile(self,N):
        """
            N is the total of packages
            type(N) = int
            type(file) = bytes 
        """
        index = int(self.widthPayload/N)
        for k in range(0,N):
            if k == N-1: #whether is the last, we must go until the final, that is, widthPayload
                self.packageList.append(self.file[index*k:self.widthPayload])
            else:
                self.packageList.append(self.file[index*k: index*(k+1)])

        

        





    