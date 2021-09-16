from django.urls import path
from . import views #. indicates current dirtory

urlpatterns=[
    path('',views.index,name='index')
    ]

