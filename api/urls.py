from django.urls import path, include

from .views import *

urlpatterns = [
    path('/register',Reg.as_view()),
    path('/test',test.as_view()),
    path('/login',Login.as_view()),
    path('/logout', Logout.as_view()),
    path('/indexindex',Index.as_view()),

    path('/getplay',GetPlay.as_view()),

]
