#!/usr/bin/python
import unicodedata
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.taxonomies import *
from wordpress_xmlrpc.methods.posts import *
from wordpress_xmlrpc.methods.users import *
from wordpress_xmlrpc.methods import *

''' from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc.methods.users import GetUser '''

wp_url = 'http://newchefreceitas.local/xmlrpc.php'
wp_username = 'admin'
wp_password = '123'

cliente = Client(wp_url, wp_username, wp_password)


def EditPostWordpressACF(post_id, client, postContent, lista_ingredientes, titulo):        
    post = WordPressPost()
    post.title = titulo
    post.content = postContent
    post.id = post_id
    post.post_type = 'osetin_recipe'
    # FUNCAO EDITADA PARA CUSTOM FIELDS
    post.custom_fields = []
    post.custom_fields.append({
        'key': 'ingredients->name',
        'value': lista_ingredientes })
    client.call(posts.EditPost(post_id, post))



def EditPostWordpressACFGalery(post_id, client, titulo, postContent, array_imgs):        
    post = WordPressPost()
    post.title = titulo
    post.id = post_id
    post.content = postContent
    post.post_format = 'gallery'
    post.post_type = 'osetin_recipe'
    # FUNCAO EDITADA PARA CUSTOM FIELDS
    post.custom_fields = []
    post.custom_fields.append({
        'key': 'gallery_images',
        'value': array_imgs })     
    client.call(posts.EditPost(post_id, post))

#imgs = [1335, 1336, 1337, 1338, 1339, 1054]
#EditPostWordpressACFGalery(1351,cliente,imgs)



def EditPostWordpressACFields(post_id, client, acf_list: list):        
    post = WordPressPost()
    #post.title = titulo
    post.id = post_id
    #post.content = postContent
    post.post_format = 'gallery'
    post.post_type = 'osetin_recipe'
    # FUNCAO EDITADA PARA CUSTOM FIELDS
    post.custom_fields = []
    for dict_acf in acf_list:
        post.custom_fields.append(dict_acf)

    client.call(posts.EditPost(post_id, post))

#imgs = [1335, 1336, 1337, 1338, 1339, 1054]
#EditPostWordpressACFGalery(1351,cliente,imgs)
""" list_dicts_acf = [{
        'key': 'recipe_cuisine',
        'value': 'brasileira'
    },
    {
        'key': '_recipe_cuisine',
        'value': 'field_5752b56e95b71'
    }]
    
EditPostWordpressACFields(19491,cliente,list_dicts_acf) """

def publishedPosts(client, ptype, pstatus, num_posts):

    published_posts = client.call(posts.GetPosts({'post_type':ptype,'post_status':pstatus,'number':num_posts}))
    return published_posts
    

# RETORNA OS POST POR TYPO E STATUS
def allPosts(client, ptype, pstatus):
    
    all_posts = client.call(posts.GetPosts({'post_type':ptype,'post_status':pstatus}))
    return all_posts


# #######################
# 
# LISTA {'post_type':ptype,'post_status':pstatus}
#    {'post_type':'osetin_recipe','tumbnail':4071}
# 
# RETORNA OS POST POR TYPO E STATUS


def get_taxterms(client, taxonomia):
    tags_list = client.call(taxonomies.GetTerms(taxonomia))
    for terms in tags_list:
        print(terms)


""" def add_category_post(client, post_tag)
    category = client.call(taxonomies.GetTerm(post_tag, 3))
    post = client.call(posts.GetPost(5))
    
    post.terms.append(category)
    client.call(posts.EditPost(post.id, post)) """


""" wp_url = 'http://localhost/chefreceitas/xmlrpc.php'
wp_username = 'admin'
wp_password = '123'
wp_site = Client(wp_url, wp_username, wp_password)
get_taxterms(wp_site, 'recipe_cuisine')

sys.exit()  """



def if_terms_exist(client, taxonomia, item):
    item = item.strip()
    tags_list = client.call(taxonomies.GetTerms(taxonomia))
    for terms in tags_list:        
        if terms.name == item:
            return terms.id    
    return 0


def add_new_terms(client, taxonomia, item):

    from wordpress_xmlrpc import WordPressTerm

    try:
        tag = WordPressTerm()
        tag.taxonomy = taxonomia
        tag.name = item
        tag.id = client.call(taxonomies.NewTerm(tag))
        return tag.id
    
    except:
        id_exist = if_terms_exist(client, taxonomia, item)
        return id_exist


# filter = {'post_type': 'acme_product', 'number': 100}
def get_posts_query(cliente, filter):
    # first, let's find some products   
    result = cliente.call(posts.GetPosts(filter))
    return result


def if_terms_exist2(client, taxonomia, item):
    item = item.strip()
    tags_list = client.call(taxonomies.GetTerms(taxonomia))
    for terms in tags_list:        
        if terms.name == item:
            return terms.id    
    return 0

def if_posts_exists(client, slug):
    offset = 0
    increment = 20
    while True:
        filter = { 'offset' : offset, 'post_type': 'osetin_recipe' }
        p = client.call(GetPosts(filter))
        if len(p) == 0:
            break # no more posts returned
        for post in p:
            if post.slug == slug:
                return(post.id)
        offset = offset + increment
    return(False)


def if_midia_exists(client, slug, object_type='attachment'):
    offset = 0
    increment = 10
    while True:
        filter = { 'post_type': object_type, 'number': increment, 'offset' : offset }
        #filter = { 'number': increment, 'offset' : offset }
        p = client.call(GetPosts(filter))
        if len(p) == 0:
            break # no more posts returned
        for post in p:
            if post.slug == slug:
                return(post.id)
        offset = offset + increment
   
    return(False)

#slug = 'cone-de-chocolate-com-avela'

#postFormats = cliente.call(GetPostFormats())
#postTypes = cliente.call(GetPostTypes())


#print(if_midia_exists(cliente, slug, 'post'))

#Searches wordpress posts based on title
# acha o primeiro post com o TITULO IGUAL
def find_id(client, title):
    offset = 0
    increment = 20
    while True:
        filter = { 'offset' : offset, 'post_type': 'osetin_recipe' }
        p = client.call(GetPosts(filter))
        if len(p) == 0:
            break # no more posts returned
        for post in p:
            if post.title == title:
                return(post.id)
        offset = offset + increment
    return(False)


# RETORNA UMA LISTA DE post_id DE POSTS 
# COM O MESMO TITULO
def find_ids_same_title(client, title):
    y = 0
    list_of_ids = []   
    offset = 0
    increment = 20
    while True:
        filter = { 'offset' : offset, 'post_type': 'osetin_recipe' }
        p = client.call(GetPosts(filter))
        if len(p) == 0:
            break # no more posts returned
        for post in p:
            if post.title == title:
                list_of_ids.append(post.id)
                y+=1
                if y == 2:
                    return(list_of_ids)    
                #return(post.id)
        offset = offset + increment

    if len(list_of_ids) != 0:
        return list_of_ids
    else:
        return(False)



# Search WordPress Tags With Python
def find_tag(wp, tag):
     p = wp.call(taxonomies.GetTerms('post_tag'))
     if len(p) == 0:
          return(False)
     for thetags in p:
         print ('looking for tag : ' , tag , ' in thetags : ' , str(thetags))
         if str(thetags) in tag:
            return(True)
     return(False)


#Searches wordpress post content for anything
def getid_search_content(wp, content):
        offset = 0
        increment = 20
        while True:
                filter = { 'offset' : offset }
                p = wp.call(GetPosts(filter))
                if len(p) == 0:
                        break # no more posts returned
                for post in p:
                        if post.content.find(content) != -1:
                                post.post_status = 'unpublish'
                                # We remove the post if its found, but you could do anything
                                wp.call(posts.EditPost(post.id, post))
                                return(post.id)
                offset = offset + increment
        return(False)






#Searches wordpress posts based on title
def buscaReceitas(wp, idImg: str, filter: dict):
    #filter = { 'offset' : 0, 'post_type': 'osetin_recipe', 'post_status': 'draft' }
    
    offset = 0
    increment = 1
    result = []

    while True:
        
        p = wp.call(GetPosts(filter))
        if len(p) == 0:
            break # no more posts returned
       
        size_filter = len(p)
        i = 0
        for post in p:
            #print(str(post.thumbnail))

            #thumbnail = {'attachment_id': str(idImg)}

            tumb_id = post.thumbnail['attachment_id']

            if tumb_id == idImg:
                
                
                #upt = time.time()
                #uptotal = upt - start_time
                #print(str(uptotal))
                #print(post)
                result.append(post)
                
                #return(post)
        i=len(result)
        print(i)

        offset = offset + increment
        if i == 30:
            return(False,result)
    
    return(False,result)


    

# post_tag = 'post_tag'
# filter: {'number': 20, 'orderby': 'count', 'order': 'DESC'}
def get_post_tags(client, post_tag, filter):
    tags = client.call(taxonomies.GetTerms(post_tag, filter))

    for tag in tags:
        print (tag.name, tag.count, tag.id)


def get_osetin_recipe_by_id(client, id):
    offset = 0
    increment = 1
    while True:
        filter = { 'offset' : offset, 'post_type': 'osetin_recipe' }
        p = client.call(GetPosts(filter))
        if len(p) == 0:
            break # no more posts returned
        for post in p:
            if post.id == id:
                return post
        offset = offset + increment
    return(False)

''' 
import sys
import os

clear = lambda: os.system('cls')
clear()

receita = get_osetin_recipe_by_id(cliente, '20378')
print(receita)

sys.exit()
 '''

def get_post_by_id(client, id, tipo, status='any'):
    offset = 0
    increment = 10    
    while True:
        if status == 'any':
            filter = { 'post_type': tipo, 'number': increment, 'offset': offset }
        else:
            filter = { 'post_type': tipo, 'post_status': status, 'number': increment, 'offset': offset }

        #filter = { 'post_status': 'publish', 'number': increment, 'offset': offset }
        
        #p = client.call(posts.GetPosts(filter))     
        p = client.call(GetPosts(filter))     
               
        if len(p) == 0:
            break  # no more posts returned        
        for post in p:
            if post.id == id:
                return post        
        offset = offset + increment        
    return(False)

# TESTE
''' import sys
import os

clear = lambda: os.system('cls')
clear()

receita = get_post_by_id(cliente, '20379', 'osetin_recipe')
print(receita)

sys.exit() '''

def remove_dup_dicts_in_list(list_of_data):
	list_of_data_uniq = []
	for data in list_of_data:
		if data not in list_of_data_uniq:
			list_of_data_uniq.append(data)
	return list_of_data_uniq


# data = {
#        'key': 'recipe_cuisine',
#        'value': 58
#        }
def AddPostMeta(client, post_id, post_type, custom_field, new_value):  
    
    new_acf_fields = []
    # cria o dict do campo personalizado para adicionar senão existir
    data = { 'key': custom_field, 'value': new_value }
    receita = get_post_by_id(client, post_id, post_type)

    if receita is False:
        print(f"post_id: {post_id}, não existe!")
        return 0

    for acf_field in receita.custom_fields:
        #print(acf_field)
        acf_field.pop('id')
        new_acf_fields.append(acf_field)

    achou = 0
    for item in new_acf_fields:
        if item['key'] == custom_field:
            item['value'] = new_value
            achou = 1
            break
            #print(item['value'])

    if achou == 0:
        new_acf_fields.append(data)

    #print(new_acf_fields)

    new_custom_fields = remove_dup_dicts_in_list(new_acf_fields)
    #print(new_custom_fields)

    post = WordPressPost()
    post.id = receita.id
    post.title = receita.title
    post.post_type = post_type
    
    post.custom_fields = []
    #post.custom_fields.pop(custom_field)

    post.custom_fields = new_custom_fields[0]
    #print(post.custom_fields)

    #post.custom_fields.append(data)

    try:
        id_out = client.call(posts.EditPost(post.id, post))
        
        print(f"Id_out: {id_out}\nPost_id: {post_id}, editado!")
    except:
        print(f"Erro\nPost_id: {post_id}, não editado")



def addpost_custom_field(client, post_id, post_type, custom_field, new_value):  
  
    data = { 'key': custom_field, 'value': new_value }
    receita = get_post_by_id(client, post_id, post_type)

    if receita is False:
        print(f"post_id: {post_id}, não existe!")
        return 0
 
    post = WordPressPost()
    post.id = post_id
    post.title = receita.title
    post.content = receita.content
    post.post_type = post_type
    
    post.custom_fields = receita.custom_fields
    #post.custom_fields.update(data)
    
    # using del + loop
    # to delete dictionary in list
    ''' lista_de_campos = receita.custom_fields
    for i in range(len(lista_de_campos)):
        if lista_de_campos[i]['key'] == custom_field:
            del lista_de_campos[i]
            break
    '''
    print(post.custom_fields)
    #print(receita.custom_fields)
    #print(lista_de_campos)

    #post.custom_fields = remove_dup_dicts_in_list(lista_de_campos)
    #post.custom_fields.update(lista_de_campos)
    #print(post.custom_fields)
    
    try:
        client.call(posts.EditPost(post.id, post))
        print(f"Post_id: {post_id}, editado!")
    except:
        print(f"Erro\nPost_id: {post_id}, não editado")



# data = {
#        'key': 'recipe_cuisine',
#        'value': 58
#        }
def update_post_custom_field(client, post_id, post_type, custom_field, new_value):  
    
    new_acf_fields = []
    # cria o dict do campo personalizado para adicionar senão existir
    data = { 'key': custom_field, 'value': new_value }
    receita = get_post_by_id(client, post_id, post_type)

    if receita is False:
        print(f"post_id: {post_id}, não existe!")
        return 0

    new_acf_fields = receita.custom_fields

    achou = 0
    for item in new_acf_fields:
        if item['key'] == custom_field:
            item['value'] = new_value
            achou = 1
            break
            #print(item['value'])

    if achou == 0:
        new_acf_fields.append(data)

    #print(new_acf_fields)

    # Remove os metas duplicados
    new_custom_fields = remove_dup_dicts_in_list(new_acf_fields)
    #print(new_custom_fields)

    post = WordPressPost()
    post.id = receita.id
    post.title = receita.title
    post.post_type = post_type   
    # Adiciona a lista de custom fields atualizada
    post.custom_fields = new_custom_fields
    #print(post.custom_fields)

    try:
        id_out = client.call(posts.EditPost(post.id, post))

        #print(f"Id_out: {id_out}\nKey: {custom_field}\n {data}\n\nPost_id: {post_id}, editado!")
        
        print(f"\nPost_id: {post_id} - Campo: {custom_field} - {data} - UPDATED\n")
    
    except:
        print(f"Erro\nPost_id: {post_id}, não editado")





''' import loading_times_min as tm

start_time = tm.show_tempo_total()

custom_field = 'recipe_difficulty'
new_value = '1'
post_id = '19970'
post_type = 'osetin_recipe'

#AddPostMeta(cliente, post_id, post_type, custom_field, new_value)

#addpost_custom_field(cliente, post_id, post_type, custom_field, new_value)
#update_post_custom_field(cliente, post_id, post_type, custom_field, new_value)

custom_field = 'recipe_serves'
new_value = '430 gramas'
update_post_custom_field(cliente, post_id, post_type, custom_field, new_value)

custom_field = 'recipe_cooking_time'
new_value = '15min'
update_post_custom_field(cliente, post_id, post_type, custom_field, new_value)


custom_field = 'quick_description'
new_value = 'Receita de Damasco Delicioso com Ricota, aprenda a preparar com Chef Receitas, receitas para todos os momentos, gostos e sabores.'
update_post_custom_field(cliente, post_id, post_type, custom_field, new_value)


print(tm.show_tempo_total(start_time))
 '''
'''
#receita = get_post_by_id(cliente, '20202', 'osetin_recipe')
#print(receita.custom_fields)

new_acf_fields = []
# cria o dict do campo personalizado para adicionar senão existir
data = { 'key': custom_field, 'value': new_value }

for acf_field in receita.custom_fields:
    #print(acf_field)
    acf_field.pop('id')
    new_acf_fields.append(acf_field)

achou = 0
for item in new_acf_fields:
    if item['key'] == custom_field:
        item['value'] = new_value
        achou = 1
        #print(item['value'])

if achou == 0:
    new_acf_fields.append(data)

print(new_acf_fields) '''