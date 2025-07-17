from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = 'oversit'
    age = 20
    return render(request,'something.html',{'name':name,'age':age})