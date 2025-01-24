import os

def listaPASTA ():
    arr = os.listdir()
    return(arr)
    
def listaPATH (path):
    arr = os.listdir(path)
    return(arr)
    

def listaHTML (path, htmlList=None):
    arr = os.listdir(path)
    for x in arr:
        extensao = x[len(x)-5:len(x)]
        #print(extensao)
        if extensao == ".html":        
            #print(x)
            if htmlList is None:
                htmlList = []
            htmlList.append(x)   
    return htmlList


def listaJPG (path, jpglist=None):
    arr = os.listdir(path)
    for x in arr:
        extensao = x[len(x)-4:len(x)]
        #print(extensao)
        if extensao == ".jpg":        
            #print(x)
            if jpglist is None:
                jpglist = []
            jpglist.append(x)   
    return jpglist