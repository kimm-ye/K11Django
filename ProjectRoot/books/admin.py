from django.contrib import admin
from books.models import Book, Author, Publisher

# 관리자모드에 테이블이 보이도록 등록한다.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
