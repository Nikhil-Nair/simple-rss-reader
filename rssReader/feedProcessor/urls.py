from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('ajax/getfeed/', views.getFeed, name = 'getFeed'),
]
