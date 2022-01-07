from django.urls import path
from . import views

# http://호스트명/board/로 들어오는 요청을 받음
app_name='board'

# 함수형 View를 사용하기 위한 URL 매핑
urlpatterns = [
    path('', views.list, name="list"),
    path('list/', views.list, name="list"),
    path('view/<int:pk>', views.view, name="view"),
    path('write/', views.write, name="write"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('delete/<int:pk>', views.delete, name="delete"),
]
