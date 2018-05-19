'''
Created on 14 de out de 2016

@author: Hugo
'''
from funcHash import *


class NohHash:
    idNoh = None
    listaDados = None
    
class TabelaHash:
    f = None
    listaDeNohs = None
    def __init__(self, fHash, tamanho):
        self.f = fHash
        self.listaDeNohs = [None]*tamanho
        
    def Insere(self,noh):
        #obtendo o id a ser convertido:
        idAntes = noh.idNoh
        #convertendo com a funcao de hash:
        idConvertido = self.f(idAntes)
        #verificando se a posicao eh invalida na tabela:
        if idConvertido < 0 or   idConvertido >= len(self.listaDeNohs):
            print('Erro! pos.',idConvertido,'Nao existe na tabela de tamanho')
            return
        elif self.listaDeNohs[idConvertido] == None:
            #ainda nao tem ninguem nesta posicao, pode inserir
            self.listaDeNohs[idConvertido] = [noh]
            
        else: #colisao!! Adicionar na lista:
            self.listaDeNohs[idConvertido].append(noh)
    def Atualiza(self, noh):
        idNovo = noh.idNoh
        idnovoCovertido = self.f(idNovo)
        for x in range(len(self.listaDeNohs[idnovoCovertido])):
            if self.listaDeNohs[idnovoCovertido][x].idNoh == idNovo:
                self.listaDeNohs[idnovoCovertido][x] = noh
                break 
            
            
        
    def Exclui(self,noh):
        idNovo = noh.idNoh
        idnovoCovertido = self.f(idNovo)
        for x in range(len(self.listaDeNohs[idnovoCovertido])):
            if self.listaDeNohs[idnovoCovertido][x].idNoh == idNovo:
                del self.listaDeNohs[idnovoCovertido][x]
                if len(self.listaDeNohs[idnovoCovertido]) == 0:
                    self.listaDeNohs[idnovoCovertido] = None
                        
        
    def Pesquisa(self, noh):
        idNovo = noh.idNoh
        idnovoCovertido = self.f(idNovo)
        for x in range(len(self.listaDeNohs[idnovoCovertido])):
            if self.listaDeNohs[idnovoCovertido][x].idNoh == idNovo:
                return self.listaDeNohs[idnovoCovertido][x].listaDados

#programa principal:

t = TabelaHash(funcaoHash, N)

entrada = input().split("!!!")
listaPrintar = []

def Cortador(string):
    listaEntrada = []
    contadorFinal = 0
    contadorInicial = 0
    for i in range(len(string)):
        
        if string[i] == ' ':
            contadorFinal = i
            corte = string[contadorInicial:contadorFinal]
            listaEntrada.append(corte)
            contadorInicial = i+1

        elif string[i]=='[':
            corte = string[i:]
            listaEntrada.append(corte)
            return listaEntrada
    listaEntrada.append(string[contadorInicial:])
    return listaEntrada
lista2 = []
for i in entrada:
    entradas = Cortador(i)
    lista2.append(entradas)

listaFinal = []
for i in range(len(lista2)):
    for j in range(len(lista2[i])):
        listaFinal.append(lista2[i][j])


for i in range(len(listaFinal)):
    if listaFinal[i] =='insert':
        k = NohHash()
        k.idNoh = int(listaFinal[i+1])
        k.listaDados = listaFinal[i+2]
        t.Insere(k)
    
    elif listaFinal[i] =='query':
        k = NohHash()
        k.idNoh = int(listaFinal[i+1])
        listaPrintar.append(t.Pesquisa(k))
        
    elif listaFinal[i] =='update':
        k = NohHash
        k.idNoh = int(listaFinal[i+1])
        k.listaDados = listaFinal[i+2]
        t.Atualiza(k)
    
    elif listaFinal[i]=='delete':
        k = NohHash
        k.idNoh = int(listaFinal[i+1])
        t.Exclui(k)
        
print('!!!'.join(listaPrintar))