from django.core import paginator
from django.shortcuts import redirect, render
from .models import Post
from boardApps.forms import WriteForm
import os
from django.conf import settings
from django.core.paginator import Paginator

def index(request):
    return render(request, 'boardApps/index.html')

def list(request):
    page = request.GET.get('page', '1')
    postlist = Post.objects.all().order_by('-id')
    
    paginator = Paginator(postlist, 10)
    postlist = paginator.get_page(page)
    
    return render(request, 'boardApps/list.html', {'postlist': postlist})


def write(request):
    if request.method == 'POST':
        try:
            Post.objects.create(
                my_name = request.POST['my_name'],
                my_pw = request.POST['my_pw'],
                my_titles = request.POST['my_titles'],
                my_contents = request.POST['my_contents'],
                my_file = request.FILES['my_file'],
            )
        except:
            Post.objects.create(
                my_name = request.POST['my_name'],
                my_pw = request.POST['my_pw'],
                my_titles = request.POST['my_titles'],
                my_contents = request.POST['my_contents'],
            )
        return redirect('/boardApps/list/')
    else:
        form = WriteForm()
    return render(request, 'boardApps/write.html', {'form':form})
            

def view(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'boardApps/view.html', {'post':post})

def edit(request, pk):
    post = Post.objects.get(pk=pk)
    
    if request.method == 'POST':
        try:
            post.my_name = request.POST['my_name']
            post.my_pw = request.POST['my_pw']
            post.my_titles = request.POST['my_titles']
            post.my_contents = request.POST['my_contents']
            post.my_file = request.FILES['my_file']
            
            os.remove(os.path.join(settings.MEDIA_ROOT, request.POST['my_file']))
        except:
            post.my_name = request.POST['my_name']
            post.my_pw = request.POST['my_pw']
            post.my_titles = request.POST['my_titles']
            post.my_contents = request.POST['my_contents']
            
        post.save()
        return redirect('/boardApps/view/'+str(pk))
    else:
        return render(request, 'boardApps/edit.html', {'post':post})

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        post.delete()
        return redirect('/boardApps/list')