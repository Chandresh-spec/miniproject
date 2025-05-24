from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import chaivarirty
from django.shortcuts import get_object_or_404
# Create your views here.


def home1(reuqest):
    return HttpResponse("this excution shows  setup is completed")

def about(request):
    chais=chaivarirty.objects.all()
    return render(request,'index.html',{'chais':chais})


def contact(request,chai_id):
    chai=get_object_or_404(chaivarirty,pk=chai_id)
    return render(request,'chai.html',{'chai':chai})