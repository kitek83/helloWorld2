from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World Fuckers\n'+
                        ' \nI feel very gooood!')


# Create your views here.
