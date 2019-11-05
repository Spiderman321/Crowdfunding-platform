from django.shortcuts import render

#coding=utf-8
from crowdfunding.models import User,Adminer,Task
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    posts = User.objects.all()
    return render_to_response('index.html',{'posts':posts})

def index(request):
    posts = Adminer.objects.all()
    return render_to_response('index.html',{'posts':posts})

def index(request):
    posts = Task.objects.all()
    return render_to_response('index.html',{'posts':posts})