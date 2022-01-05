from django.urls import path
from . import views
'''
클래스형 뷰를 사용하기 위한 URLConf 설정. 각 항목마다 as_view() 함수를 사용한다.

path() 함수 : route, view 2개의 필수인자와 kwargs, name 2개의 선택인수를 받는다.
    route : URL 패턴을 표현하는 문자열로 URL스트링이라고 한다.
    view : URL 스트링이 매칭되면 호출되는 View 함수. HttpRequest 객체와
        URL스트링에서 추촐된 항목이 View 함수의 인자로 전달된다.
    kwargs : URL 스트링에서 추출된 항목 외에 추가적인 인자를 View 함수로
        전달할 때 파이썬의 딕셔너리 타입으로 인자를 정의한다.
    name : 각 URL 패턴별로 별칭을 붙여준다. 여기서 정한 이름은 주로 템플릿에서
        사용하게 된다.
'''
app_name="books"
urlpatterns = [
    path('', views.BooksModelView.as_view(), name="index"),
    path('book/', views.BookList.as_view(), name="book_list"),
    path('author/', views.AuthorList.as_view(), name="author_list"),
    path('publisher/', views.PublisherList.as_view(), name="publisher_list"),
    path('book/<int:pk>/', views.BookDetail.as_view(), name="book_detail"),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name="author_detail"),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name="publisher_detail"),
]
