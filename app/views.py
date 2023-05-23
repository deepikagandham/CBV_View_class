from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# FBV for returning string

def FBV_string(request):
    return HttpResponse('This is FBV string')
# CBV for returning string

class CBV_string(View):
    def get(self,request):
        return HttpResponse('This is CBV string')

# FBV for returning html page

def FBV_html(request):
    return render(request,'FBV_html.html')

# CBV for returning HTML page

class CBV_html(View):
    def get(self,request):
        return render(request,'CBV_html.html')

# Handling form by using FBV

def fbv_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method == 'POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')
    return render (request,'fbv_form.html',d)

# Handling form by using cbv

class cbv_form(View):
    def get(self,request):
        TFO=TopicForm()
        d={'TFO':TFO}
        
        return render(request,'cbv_form.html',d)
     
    def post(self,request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')
        
