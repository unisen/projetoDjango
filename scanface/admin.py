from django.contrib import admin

# Register your models here.


""" CREATE TABLE `tbl_facelogin` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `type_user` varchar(100) NOT NULL,
  `cpf_user` varchar(20) NOT NULL,
  `name_user` varchar(300) NOT NULL,
  `login_images` varchar(300) DEFAULT NULL,
  `dateRegistered` varchar(50) DEFAULT NULL,
  `registro` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci; """

""" 
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language) """