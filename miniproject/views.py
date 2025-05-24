from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def home1(reuqest):
    return HttpResponse("this excution shows  setup is completed")