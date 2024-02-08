from django.shortcuts import render
from testapp.forms import LoginForm
import datetime
# Create your views here.
def home_view(request):
    form = LoginForm()
    return render(request,'testapp/home.html',{'form':form})

def date_time(request):
    name = request.GET['name']
    response = render(request,'testapp/datetime.html',{'name':name})
    response.set_cookie('name',name)
    return response

def result_view(request):
    name = request.COOKIES.get('name')
    date_time = datetime.datetime.now()
    return render(request,'testapp/results.html',{'name':name,'date_time':date_time})
