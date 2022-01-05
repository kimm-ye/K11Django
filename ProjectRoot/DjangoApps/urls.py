from django.contrib import admin
from django.urls import path
# 외부에 있는 urls.py를 인클루드 하기 위한 임포트
from django.urls import include
'''
해당 URLconf는 프로젝트 레벨이므로 livepolls앱의 views파일(모듈)을 
임포트해야만 접근할 수 있다.
'''
from livepolls import views

'''
장고에서의 URL패턴 작성법
    path(요청URL패턴, 처리할 view의 함수명, URL의 별칭) 
    여기서 별칭은 필수사항은 아니다.
'''

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls), # 관리자모드
    # http://127.0.0.1:8000/
    path('', views.main, name='main'), # 로켓화면 대신 메인화면으로 대체할 예정
    
    # 방법1 : 1개의 파일에 작성
    # http://127.0.0.1:8000/livepolls/
    # path('livepolls/', views.index, name='index'), # 등록된 투표의 질문을 출력
    # path('livepolls/<int:question_id>/', views.detail, name='detail'),
    # path('livepolls/<int:question_id>/results/', views.results, name='results'),
    # path('livepolls/<int:question_id>/vote/', views.vote, name='vote'),

    # 방법2: 2개의 파일에 작성
    path('livepolls/', include('livepolls.urls')), # 앱1 : 설문 관리 앱
    path('tempapps/', include('tempapps.urls')),   # 앱2 : 템플릿 문법 앱
    path('books/', include('books.urls')),         # 앱3 : 도서관리 앱
]
'''
방법1의 경우 Url패턴이 변경되면 모든 항목을 수정해야 하므로 불편하다.
하지만 방법2와 같이 파일을 2개로 나누게되면 하나의 패턴을 위한 네임스페이스가
생성되는 개념이므로 한번만 수정하면 되서 편리하다.
즉, livepolls/로 들어오는 모든 요청을 livepolls앱 하위의 urls.py로 전달한다.
'''