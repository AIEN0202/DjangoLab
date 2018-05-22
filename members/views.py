from django.shortcuts import render

# Create your views here.
def index(request):
    # print(request.method)
    # return HttpResponse("<h2>Home Index</h2>", content_type="text/html")
    title="Members"
    return render(request,'members/index.html',locals())
