import os

def listaArquivos (path):
    arr = os.listdir(path)
    return arr


def listaHTMLs (path, htmlList=None):
    
    arr = os.listdir(path)
    i = 1 
    for x in arr:
        extensao = x[len(x)-5:len(x)]
        #print(extensao)
        if extensao == ".html":
            #print(x)
            i += 1
            if htmlList is None:
                htmlList = []
            htmlList.append(x)

    #print('Total: '+str(i))  
    return htmlList


def listaTXTs (path, txtList=None):
    
    arr = os.listdir(path)
    i = 1 
    for x in arr:
        extensao = x[len(x)-4:len(x)]
        #print(extensao)
        if extensao == ".txt":
            #print(x)
            i += 1
            if txtList is None:
                txtList = []
            txtList.append(x)

    #print('Total: '+str(i))  
    return txtList



def lista_imagens_da_receita(id,path):

    i = 0
    lista_de_arquivos = os.listdir(path)
    # TOTAL DE ARQUIVOS NO DIRETORIO
    #print(len(lista_de_arquivos))
    lista_imgs = []
    for imagem in lista_de_arquivos:
       
        imgsplit = imagem.split('_')

        if(imgsplit[0] == str(id)):
            lista_imgs.append(imagem)
            i+=1        
    
    return lista_imgs, i


def lerListaCozinhaLinks(arq):
    f = open(arq, "r")
    texto = f.read()
    f.close()
    return str(texto)

def lerArquivoTXTutf8(arq):
    f = open(arq, "r")
    texto = f.read()
    f.close()
    return str(texto)

def lerArquivoEncodingUTF(arq):
    f = open(arq, "r", encoding='UTF-8')
    texto = f.read()
    f.close()
    return str(texto)



def get_folder_sizes(path_origem):
    arr = os.listdir(path_origem)

    total_size = 0

    for imgs in arr:
        file_size = os.path.getsize(path_origem+imgs)
        total_size += file_size

        #print("File Size is :", file_size, "bytes")
        #break

    size_in_gigabytes = total_size/(1024*1024*1024)
    total = ("%.2f" % size_in_gigabytes)
    total = total + " GB"

    if size_in_gigabytes < 1:
        size_in_megabytes = total_size/(1024*1024)
        total = ("%.2f" % size_in_megabytes)
        total = total + " MB"


    return total, size_in_gigabytes


def pesquisaDiretorio (path, filename):
    
    arr = os.listdir(path)
    i = 1
    txtList = []

    for x in arr:
        extensao = x[len(x)-5:len(x)]
        #print(extensao)
        if extensao == ".webp":
            #print(x)
            i += 1
            arquivo_lido = x[0:len(filename)]
            if filename == arquivo_lido:
                txtList.append(x)

    #print('Total: '+str(i))  
    return txtList



""" fileimage = 'imagens/docinho_ricota.webp'
imagem = fileimage.split('/')
fileimage = imagem[1]
imagem = fileimage.split('.webp')
fileimage = imagem[0]

print(fileimage)

print(pesquisaDiretorio('imagens', fileimage)) """




""" cpath = 'cozinha_mexicana/'
dir_orign = '../SUPERSCRAPER/cozinhas/mexican recipes/images/'
"""
""" tsize, size_gigas = get_folder_sizes('tesao/')
print(size_gigas)
print(tsize) """


#numero da pagina de arquivos da categoria (thai recipes)
""" num = 1 # Page 1 archives recipes page
diretorio = 'cozinhas/'
cozinha = 'thai recipes'

# cozinhas/thai recipes
pasta = str(diretorio)+str(cozinha)
# selectiona para achar o path da pasta
os.chdir(pasta)
# pega o path da pasta seleciona
path = os.getcwd()
path_fisico = path + '\\'
print(path_fisico)

arrArquivos = listaArquivos(path_fisico)
print(len(arrArquivos))

for arquivo in arrArquivos:
    print(arquivo)

arquivo = pasta + '/page-'+str(num)+'.txt' """






#path_fisico = os.environ['PYTHONPATH'].split(os.pathsep)
#print(path_fisico)

#listaHTMLs(path_fisico)
#pasta = "./"+str(diretorio)+str(cozinha[0])