def limpaString(txt):
    listofchars = ['!','#','$','%',',',';','&reg','*','(',')','?','^','~','´',"'",'=','[',']','}','{']	
    for rchar in listofchars:
        txt = txt.replace(rchar,'')  
    return (txt)