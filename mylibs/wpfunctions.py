import unicodedata
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc.methods.users import GetUser

import modulos.functions_geral as gfunction
import libs.oslistagem as ls

global placeholderId

#placeholderId = 4071 #8957
placeholderId = 19629


global cliente
url_xmlrpc='http://newchefreceitas.local/xmlrpc.php'
user_login='admin'
pass_login='123'

cliente = Client(url_xmlrpc, user_login, pass_login)


global tipo_de_post
tipo_de_post = 'osetin_recipe'



def uploadImg(client,slug,img):
    
    file_image = img    
    if file_image == 'imagens/placeholder.png':        
        attachment_id = placeholderId    
    else:
        # prepare metadata
        # choosen type        
        # mimetype = 'image/jpeg'  # mimetype
        # Convertido para Webp
        mimetype = 'image/webp'
        # Slug
        #mimetypeslug = '.jpeg'
        mimetypeslug = '.webp'        
        slug_limpo = gfunction.limpaString(slug)
        
        data = {
                'name': slug_limpo + mimetypeslug,
                'type': mimetype,  # mimetype
        }
        
        # read the binary file and let the XMLRPC library encode it into base64
        try:           
            # Código para fazer uploads de imagens Webp
            file_image = file_image.replace('.jpeg','.webp')
            
            with open(file_image, 'rb') as img:
                    data['bits'] = xmlrpc_client.Binary(img.read())

            response = client.call(media.UploadFile(data))
            # response == {
            #       'id': 6,
            #       'file': 'picture.jpg'
            #       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
            #       'type': 'image/jpeg',
            # }
            
            #PEGA O ID DA IMAGEM SALVA NO WORDPRESS
            attachment_id = response['id']        
                    
            imagemName = file_image
            imagemName = str(unicodedata.normalize('NFKD', imagemName).encode('ASCII', 'ignore'))
            imagemName = imagemName[2:-1]        

        except:
            # Editado 05/01/2022 
            # Procura na pasta imagens arquivo com nome semelhante sem as dimensoes no nome do arquivo
            try:
                fileimage = img
                imagem = fileimage.split('/')
                fileimage = imagem[1]
                imagem = fileimage.split('.webp')
                nome_arquivo = imagem[0]
                #print(fileimage)

                # Função que faz a busca dentro do diretorio de acordo com 
                # o nome puro do arquivo
                lista_pesquisa = ls.pesquisaDiretorio('imagens', nome_arquivo)           
                # Código para fazer uploads de imagens Webp
                file_image = 'imagens/' + lista_pesquisa[len(lista_pesquisa)-1]
                
                with open(file_image, 'rb') as img:
                        data['bits'] = xmlrpc_client.Binary(img.read())

                response = client.call(media.UploadFile(data))
                # response == {
                #       'id': 6,
                #       'file': 'picture.jpg'
                #       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
                #       'type': 'image/jpeg',
                # }
                
                #PEGA O ID DA IMAGEM SALVA NO WORDPRESS
                attachment_id = response['id']                       
                imagemName = file_image
                imagemName = str(unicodedata.normalize('NFKD', imagemName).encode('ASCII', 'ignore'))
                imagemName = imagemName[2:-1]  

            except:

                # Change to *.png
                #fileImage = 'imagens/placeholder.png'                
                file_image = 'imagens/placeholder.webp'                
                attachment_id = placeholderId
                    
    return attachment_id


def createTaxonomies(strcats, strtags):

    # MONTA A VARIAVEL postTerms
    # MONTA A VARIAVEL post.terms_names = { dictionary }
    global tags
    global categorias

    if (strtags == '' and strcats == ''):
        categorias = []
        tags = []  

    elif strcats == '':
        categorias = []
        tags = strtags.split(",")
        
    elif strtags == '':
        tags = []
        categorias = strcats.split(",")
      
    else:    
        tags = strtags.split(",")
        categorias = strcats.split(",")
        
    cat_strip = []

    for cat in categorias:
        #print(cat.strip())
        strip_str = cat.strip()
        cat_strip.append(strip_str)
    
    categorias = list(dict.fromkeys(cat_strip))
    
    # Retira a categoria ambígua
    existe_termo = categorias.count("Receitas Fáceis")
    if (existe_termo > 0):
        categorias.remove("Receitas Fáceis")
    
    postTerms = {
        'post_tag': tags,
        'category': categorias
    }
    
    return postTerms



def salvaPost(client, titulo, slug, attachment_id, postStatus, postContent, postTerms, commentStatus):
    
    # set to the path to your file
    #print(filename) 'http://todasreceitas.local/wp-content/uploads/2020/11/placeholder.jpg' ID 5592
       
    post = WordPressPost()
    post.title = titulo
    post.slug = slug
    post.content = postContent
    post.terms_names = postTerms
    
    # add em 27/12/2021
    # define o comentario open
    post.comment_status = commentStatus
    
    # Se o post é rascunho, comentários closed
    # Editada 05/01/2022
    if attachment_id == placeholderId:
        postStatus = 'draft'
        commentStatus = 'close'

    post.post_status = postStatus

    # add em 27/12/2021
    # define o comentario open
    post.comment_status = commentStatus
    
    post.thumbnail = attachment_id
    post.post_type = tipo_de_post
    
    post.id = client.call(posts.NewPost(post))
   
    return post.id

