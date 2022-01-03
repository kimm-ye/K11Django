from django.urls import path
from . import views

# app_name은 차후 URL처리를 위한 네임스페이스로 활용된다.
app_name = 'livepolls'

# 네임스페이스로 처리되므로 livepolls/를 제외한 URL패턴을 기술하면 된다.
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name='detail'), # /livepolls/일련번호/
    path('<int:question_id>/results/', views.results, name='results'), # /livepolls/일련번호/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # /livepolls/일련번호/vote/
]
