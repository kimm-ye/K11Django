from django.core import paginator
from django.shortcuts import redirect, render
from .models import Post
import os
from django.conf import settings
from django.core.paginator import Paginator

# 게시판 앱의 첫화면 (원래 로켓화면인데 index.html로 넘어갈 수 있게 처리)
def index(request):
    return render(request, 'board/index.html')

# 게시판 목록
def list(request):
    # ?page=페이지번호 형태로 넘어오는 파라미터를 받아서 사용한다.
    # 파라미터가 없다면 1로 설정한다.
    page = request.GET.get('page', '1')
    # Post 테이블의 모든 레코드를 id(일련번호:PK)의 내림차순으로 가져온다.
    postlist = Post.objects.all().order_by('-id')
    
    # Paginator 클래스를 통해 게시물 10개씩 잘라서 가져온다.
    paginator = Paginator(postlist, 10)
    # page번호를 통해 현 페이지에 출력할 게시물을 가져온다.
    postlist = paginator.get_page(page)
    
    # 템플릿을 렌더링 한다.(마치 forward를 걸듯이)
    return render(request, 'board/list.html', {'postlist':postlist})

# 글쓰기
def write(request):
    # 전송방식이 POST라면 submit이므로 폼값을 테이블에 입력한다.
    if request.method=='POST':
        # 페이징 처리를 위한 더미데이터 200개 입력시 사용
        # for i in range(200):
        try:
            # 파일첨부가 있는 경우 여기서 insert됨
            '''
            문자열 + 정수 형태로 연결하면 파이썬에서는 에러가 발생한다.
            따라서 정수를 문자열로 변경하기 위해 "문자열 + str(정수)" 형태로
            기술해야 한다.
            '''
            Post.objects.create(
                titles=request.POST['titles'],
                # titles=request.POST['titles'] + "-" + str(i),
                contents=request.POST['contents'],
                # 파일첨부를 하지 않으면 여기서 예외 발생됨
                mainphoto=request.FILES['mainphoto'],
            )
        except:
            # 파일첨부를 하지 않은 경우이므로 제목과 내용만 입력함
            Post.objects.create(
                titles=request.POST['titles'],
                # titles=request.POST['titles'] + "-" + str(i),
                contents=request.POST['contents'],
            )
            # create()를 통해 insert 처리
        # 입력이 처리되었다면 리스트로 이동한다.
        return redirect('../list')  
    # 전송방식이 GET이라면 글쓰기 페이지로 진입한다.      
    return render(request, 'board/write.html')

# 글 상세보기
def view(request, pk):
    # 일련번호에 해당하는 게시물 하나를 select 한다.
    post = Post.objects.get(pk=pk)
    return render(request, 'board/view.html', {'post':post})

# 글 수정하기
def edit(request, pk):
    # 일련번호를 통해 기존 게시물 가져오기
    post = Post.objects.get(pk=pk)
    
    if request.method=='POST':
        try:
            post.titles=request.POST['titles']
            post.contents=request.POST['contents']
            post.mainphoto=request.FILES['mainphoto']
            
            print(os.path.join(settings.MEDIA_ROOT, request.POST['prevphoto']))
            os.remove(os.path.join(settings.MEDIA_ROOT, request.POST['prevphoto']))
        except:
            post.titles=request.POST['titles']
            post.contents=request.POST['contents']
        # 폼값 처리후 save()함수를 통해 update 처리함
        post.save()
        # 수정처리가 완료되면 상세보기 페이지로 이동함
        return redirect('../view/'+str(pk))
    else:
        # 전송방식이 GET이라면 수정하기로 진입함
        return render(request, 'board/edit.html', {'post':post})
    
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method=='GET':
        post.delete()
        return redirect('../list')

