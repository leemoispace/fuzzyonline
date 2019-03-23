from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #下面这句该怎么写才能调用函数？？？
    #url(r'^submit', views.submit)
]