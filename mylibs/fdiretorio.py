# FUNCAO QUE CRIA O DIRETORIO DA PAGINA PARA SALVAR OS ARQUIVOS DAS
# por PAGINA
#
def CriaDiretorio(path_dir):    
    import os
    #dirTemp = './temp'
    dirTemp = path_dir
    
    try:
        os.mkdir(dirTemp)
    except OSError:
        os.rmdir(dirTemp)
        os.mkdir(dirTemp)


# dir = 'icones_de_ingredientes/'
# retorna o caminho do diretorio criado
def CriaDirCustom(dir, custom_name):
    try:
        newdir = './'+dir+custom_name
        CriaDiretorio(newdir)
        return (dir + custom_name + '/')
    except:
        print('Ops... Erro')
        return 0