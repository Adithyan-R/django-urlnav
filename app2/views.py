from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_home(args):
    return render(args,'app2.html')
    
def app2_msg(args):
    return HttpResponse('App2 message sent')

    
    