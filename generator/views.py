from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):
    
    characters= list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):# this checks if uppercase is on in password url
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('special'):
        characters.extend(list('!@#%^&*()'))
        
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
                
    length=int(request.GET.get('length',12))#12 is the default length value
    
    thepassword=''
    
    for x in range(length):
        thepassword+= random.choice(characters)
        
    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    authorname='Kwin'
    return render(request,'generator/about.html',{'about':authorname,'about1':'Hi you found me'})