from django.urls import path
from . import views
app_name="members"
urlpatterns = [
    #http://localhost:8000/members
    path('',views.index,name="index")
]