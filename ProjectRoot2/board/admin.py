from django.contrib import admin
from .models import Post

# 관리자모드에 Post테이블 등록
admin.site.register(Post)
