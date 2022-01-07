import django
from django.db import models
from django.shortcuts import render
# 클래스형 제네릭뷰를 사용하기 위한 임포트
from django.views.generic.base import TemplateView  # 템플릿 뷰
from django.views.generic import ListView  # 리스트 뷰
from django.views.generic.detail import DetailView  # 디테일 뷰
# 레코드 조회를 위한 모델 클래스 임포트
from books.models import Book, Author, Publisher

# books 애플리케이션 첫 화면을 출력
class BooksModelView(TemplateView):  # 해당 클래스는 TemplateView를 상속하여 정의
    # TemplateView를 사용하는 경우 해당 클래스변수를 오버라이딩 해야한다.
    template_name='books/index.html'  # 템플릿 파일경로를 지정한다.
    # 함수형 뷰처럼 render() 함수를 통해 반환하지 않아도 자동으로 호출된다.
    
    # 템플릿으로 전달할 데이터가 있는 경우 get_context_data()를 오버라이딩 한다.
    def get_context_data(self, **kwargs): # 자동완성 지원됨
        # 오버라이딩 하는 경우 반드시 super()를 첫줄에 선언해야 한다.
        context = super().get_context_data(**kwargs)
        # 템플릿으로 전달할 데이터 저장
        context['model_list'] = ['Book', 'Author','Publisher']
        # return 도 필수적으로 필요하다.
        return context

'''
제네릭뷰 중 ListView를 사용하여 리스트 구현
    : ListView를 상속받는 경우 해당 모델 클래스를 템플릿으로 전달하는 것 만으로
    리스트구성, 컨텍스트 변수 저장 및 전달이 자동으로 처리된다.
    또한 디폴트로 지정되는 2가지가 있는데
    첫째 컨택스트 변수로 object_list를 사용한다.
    둘째 템플릿 파일명은 "모델명소문자_list.html"로 지정된다.
    
    원래는 변수를 담아서 context로 넘겼어야 하는데 context={}하고 render (,context)
    여기서는 하지 않았다. 그걸 ListView가 알아서 자동으로 해주기 때문이다.
'''
class BookList(ListView):
    # 1. Book 테이블로부터 모든 레코드를 가져와서 컨텍스트 변수 object_list에 저장한다.
    # 2. 템플릿 파일은 "books/book_list.html"과 같이 지정되어 컨텍스트 변수가 전달된다.
    # 이 부분이 자동으로 처리된다.
    model = Book
    
class AuthorList(ListView):
    model = Author
    
class PublisherList(ListView):
    model = Publisher


'''
제네릭 뷰 중 DetailView를 사용하여 상세페이지 구현
    : DetailView를 상속하는 경우 특정 레코드 하나를 조회한 후 컨텍스트
    변수에 저장한다. URLConf에서 지정한 파라미터를 통해 특정 레코드 하나를 
    조회한 후 템플릿으로 전달하게 된다.
'''
class BookDetail(DetailView):
    # 1. 테이블로부터 조회한 값은 object라는 변수명으로 컨텍스트에 저장한다.
    # 2. "모델명소문자_detail.html" 이라는 템플릿 파일명을 찾아 렌더링 한다.
    model = Book
    
class AuthorDetail(DetailView):
    model = Author
    
class PublisherDetail(DetailView):
    model = Publisher