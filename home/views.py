from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    title = "Home Index"
    name = "Steven"  
    now = datetime.datetime.now()

    users = [{"name":"Jack","age":30,"email":"Jack@gmail.com"},{"name":"Tom","age":38,"email":"Tom@gmail.com"},{"name":"Mary","age":25,"email":"Mary@gmail.com"}]
    # print(request.method)
    # return HttpResponse("<h2>Home Index</h2>", content_type="text/html")
    # return render(request,'home/index.html',{"title":"首頁...","name":"Fiona"})
    return render(request,'home/index.html',locals())

def about(request):
    # return HttpResponse("<h2>Home About</h2")
    # return redirect("/contact")
    title="about page"
    return render(request, 'home/about.html',locals())

def contact(request):
    # return HttpResponse("<h2>Home Contact</h2>")
    title="contact page"
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "guest"
    if 'age' in request.GET:
        age = request.GET['age']
    else:
        age = 0
        
    return render(request, 'home/contact.html',locals())

def contact1(request,name,age):
    title="Contact1"
    return render(request,'home/contact1.html', locals())
