from django.shortcuts import render,redirect
# Create your views here.
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import IRC_API
from .forms import IRCForms
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect 
from django.http import JsonResponse



import datetime 


def Irc_View(request):
 
    if request.method == 'POST':
        url = request.POST.get('url')
        date_time = request.POST.get('date_time')
        print("recieved datetime",date_time)
    
        print("current datetime",datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        current_datetime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        form=IRCForms(data=request.POST)

        if form.is_valid():
            
            form.save()
            
            if date_time==current_datetime:
                return redirect(url)
            else:
                return  HttpResponse("check your date and time")
        
        else:
            print(form.errors)
    else:
        form=IRCForms()        
    return render(request,'basic_app/a.html',{'form':form})


def Ping_view(request):
    responseData = {
        'status': "ok",
         
    }
    return JsonResponse(responseData)
