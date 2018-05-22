from django.urls import path
from . import views
app_name="home"
urlpatterns = [
    #http://localhost:8000
    path('',views.index,name="index"),
    #http://localhost:8000/about
    path('about/',views.about,name="about"),
    #http://localhost:8000/contact
    path('contact/',views.contact,name="contact"),
    #http://localhost:8000/contact/mary/20
    path('contact/<str:name>/<int:age>',views.contact1,name="contact1")
]

