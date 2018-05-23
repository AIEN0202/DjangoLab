from django.urls import path
from . import views

app_name="product"
urlpatterns = [
    #http://localhost:8000/product
    path('',views.index,name="index"),
    #http://localhost:8000/product/create
    path('create/',views.create,name="create"),
    #http://localhost:8000/product/update
    path('update/<int:id>',views.update,name="update"),
    #http://localhost:8000/product/delete/1
    path('delete/<int:id>',views.delete,name="delete")
]