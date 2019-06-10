from django.urls import path, include

from .views import *

urlpatterns = [
    path('register',Reg.as_view()),
    path('test',test.as_view()),
    path('login',Login.as_view()),
    path('logout', Logout.as_view()),
    path('indexindex',Index.as_view()),

    path('getplay',GetPlay.as_view()),
    path('addplay',AddPlay.as_view()),
    path('updateplay',UpdatePlay.as_view()),
    path('delplay',DelPlay.as_view()),

    path('getscheme',GetScheme.as_view()),
    path('addscheme',AddScheme.as_view()),
    path('updatescheme',UpdateScheme.as_view()),
    path('delscheme',DelPlay.as_view()),

    path('getstudio',GetStudio.as_view()),
    path('addstudio',AddStudio.as_view()),
    path('updatestudio',UpdateStudio.as_view()),
    path('delstudio', DelStudio.as_view()),

    path('getticket',GetTicket.as_view()),
    path('addticket',AddTicket.as_view()),
    path('updateticket',UpdateTicket.as_view()),
    path('delticket',DelTicket.as_view()),

    path('getpic',GetPic.as_view()),
    path('getsaledtic',GetSaleTic.as_view()),

]
