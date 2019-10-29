from django.shortcuts import render

#coding=utf-8
from crowdfunding.models import Sponsor
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    posts = Sponsor.objects.all()
    return render_to_response('index.html',{'posts':posts})
