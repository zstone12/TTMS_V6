from django.urls import path, include

from .views import *

urlpatterns = [
    path('', show_plays),
    path('show_schemes',show_shemes),
    path('show_schemes/show_seats',show_seats),
    path('show_schemes/show_ticket',show_ticket),

]
