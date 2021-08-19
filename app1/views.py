from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_home(args):
    return render(args,'app1.html')
    
def app1_msg(args):
    return HttpResponse('App1 message sent')

    
    