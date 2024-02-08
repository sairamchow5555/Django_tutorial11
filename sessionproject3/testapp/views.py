from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

def age_view(request):
    print(request.COOKIES)
    username = request.GET['name']
    response = render(request,'testapp/age.html',{'name':username})
    response.set_cookie('name',username)
    return response

def gf_view(request):
    print(request.COOKIES)
    username = request.COOKIES['name']
    age = request.GET['age']
    response = render(request,'testapp/gf.html',{'name':username,'age':age})
    response.set_cookie('age',age)
    return response

def results_view(request):
    print(request.COOKIES)
    username = request.COOKIES['name']
    age = request.COOKIES['age']
    gfname = request.GET['gf']
    response = render(request,'testapp/results.html',{'name':username,'age':age,'gf':gfname})
    return response
