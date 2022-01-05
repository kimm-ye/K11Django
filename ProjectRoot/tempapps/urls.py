from django.urls import path
from . import views

app_name='tempapps'
urlpatterns = [
    path('', views.index, name='index'),
    path('template.filter/', views.templateFilter, name="my_filter"), # 템플릿 필터
    path('template.tag/', views.templateTag, name="my_tag"), # 템플릿 태그
    path('form.create/', views.formCreate, name='formCreate'), # 폼 사용하기
    path('thanks/', views.thanks),
    path('boardWrite/', views.boardWrite),
]
