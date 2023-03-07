from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_first(request):
    return HttpResponse('<marquee><h1> this is app2 first function </marquee></h1>')


def app2_second(request):
    return HttpResponse('<marquee><h1> this is app2 second function </marquee></h1>')