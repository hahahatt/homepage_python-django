from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from polls.forms import *
from .models import *
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def firstpg(request):
    return render(request, 'polls/firstpg.html')

def index(request):
    return render(request,'polls/index_1.html')

def content_1(request):
    return render(request,'polls/content_1.html')

def content_2(request):
    return render(request, 'polls/content_2.html')

def content_1_1(request):
    return render(request, 'polls/content_1_1.html')

def content_1_2(request):
    return render(request, 'polls/content_1_2.html')

def content_3(request):
    return render(request, 'polls/content_3.html')
def content_3_1(request):
    return render(request, 'polls/content_3_1.html')

def content_3_2(request):
    return render(request, 'polls/content_3_2.html')

def content_3_3(request):
    return render(request, 'polls/content_3_3.html')

def board(request):
    if request.method == 'POST':
        title=request.POST['title']
        content=request.POST['content']
        user=request.user
        pub_date=timezone.now()
        board=Board(
            title=title,
            content=content,
            user=user,
            pub_date=pub_date,
        )
        board.save()
        return redirect('board')
    else:
        boardForm=BoardForm
        board=Board.objects.all()
        context={
            'boardForm' : boardForm,
            'board' : board,
        }
        return render(request,'polls/board.html',context)

def boardEdit(request,pk):
    board=Board.objects.get(id=pk)
    if request.method=='POST':
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.user=request.user

        board.save()
        return redirect('board')
    else:
        boardForm=BoardForm
        return render(request,'polls/update.html',{'boardForm':boardForm})

def boardDelete(request,pk):
    board=Board.objects.get(id=pk)
    board.delete()
    return redirect('board')

def detail_content(request,pk):
    board=Board.objects.get(id=pk)
    return render(request, 'polls/detail_content.html',{'board':board})

def create_reply(request, pk):
    b = Board.objects.get(id = pk)
    b.reply_set.create(comment=request.POST['comment'], rep_date=timezone.now())
    return HttpResponseRedirect(reverse('detail',args=(pk,)))