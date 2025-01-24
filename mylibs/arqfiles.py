#######################################################################################
# 
# FUNÇÕES QUE MONITORAM O ESTADO DA IMPORTAÇÃO DE ACORDO COM A CONTAGEM DO LOOP
# PEGA O INICIO DO LOOP DENTRO DO ARQUIVO import-status.txt
# que fica no mesmo diretorio do arquivo
# 
# e no FINAL DO LOOP graça o contador do LOOP no mesmo arquivo ATUALIZANDO
# AGORA O LOOP e comandado pelo arquivo .txt para atualizar a contagem
# CASO O PROGRAME PARE E REINICIE - ELA REINICIARÁ DO PONTO ONDE PAROU
# 
#######################################################################################

import os
import sys

def getStatusImport():    
    f = open("import-status.txt", "r")
    x = int(f.read())
    f.close
    return x 


def updateStatusImport(status):        
    f = open("import-status.txt", "w")    
    f.write(str(status))
    f.close()
    

def linesArquivo(arquivo):
    arquivo = open(arquivo, "r")
    linhas = arquivo.readlines()
    arquivo.close
    return linhas

# cria o arquivo e retorna seu nome
def criaArquivo(arquivo, param):
    
    import pickle    
    try:
		
        binary_file = open(arquivo, 'ab')
        pickle.dump(list, binary_file)
        binary_file.close()    
    except:
        print("Something went wrong")


# Verifica se um arquivo existe pelo path do main file    
def check_file_exists(fp):
    import os  
    if(os.path.isfile(fp)):
        return(1)
        #print('existe')
    else:
        return(0)
        #print('nao existe')
 

# path: logs/
# file_name: status-log.txt
def cria_arquivo_de_log(path, file_name):
    fp = path+file_name    
    if(check_file_exists(fp)==0):
        print(f"Criando o arquivo: {file_name}")
        arquivo = open(fp, "a+")
        arquivo.close()
    else:
        print(f"Arquivo: {fp} existe!")

     
# file path: modulos/testes.py
# Função lê a partir do diretório que executa o main file
#check_file_exists('teste01.txt')

# funcao le um arquivo com uma linha de informação numérica
# usada mais para ler uma linha do arquivo
# e retornar este valor como INT
def getNumStatus(arquivo):    
    f = open(arquivo, "r")
    x = int(f.read())
    f.close
    return x 

# funcao para atualizar um arquivo
def updateArquivo(arquivo, status):        
    f = open(arquivo, "w")    
    f.write(str(status))
    f.close()
    
# funcao que le um arquivo e escreve uma nova linha no final dele
# atualizando com uma linha com informação nova
# 
def appendArquivo(arquivo,status):
    f = open(arquivo, "a")
    f.write(str(status+'\n'))
    f.close

def appendArquivo2(arquivo, status):    
    # abre o arquivo
    f = open(arquivo, "r")
    # le o arquivo e pega toda a informação contida nele
    x = str(f.read())    
    # soma a informações do arquivo a nova linha
    # e insere a nova linha no arquivo novamente
    status = "\n" + x + "\n" + status
    # abre o arquivo para escrita
    f = open(arquivo, "a")
    # grava o novo status
    f.write(str(status))
    # fecha o arquivo
    f.close

def logTreads(arquivo, status):
    f = open(arquivo, "w")
    f.write(status)
    f.close

def readTread(arquivo):
    f = open(arquivo, "r")
    x = str(f.read())
    return x

def updateStatusTotal(status):
    
    f = open("total-status.txt", "r")
    x = str(f.read())    
    
    status = "\n" + x + "\n" + status

    f = open("total-status.txt", "w")
    f.write(str(status))
    f.close
