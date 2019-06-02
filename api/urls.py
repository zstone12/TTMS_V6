from django.urls import path, include

from .views import *

urlpatterns = [
    path('/login',Reg.as_view()),
    path('/test',test.as_view()),
]
