from django.shortcuts import render, HttpResponse, redirect
from app01 import models

from django.utils import timezone


# Create your views here.

def add_scheme(requests):
    if requests.method == 'POST':
        play = requests.POST.get('play')
        studio = requests.POST.get('studio')
        # print(play, studio)
        year = requests.POST.get('year')
        month = requests.POST.get('month')
        day = requests.POST.get('day')
        hour = requests.POST.get('hour')
        minute = requests.POST.get('minute')
        # print(type(year),type(month),type(day),type(hour),type(minute))
        time = year + '-' + month + '-' + day + ' ' + hour + ':' + minute

        # 2019-1-1 15:13
        obj = models.Scheme.objects.create(play_id=play, studio_id=studio, start_time=time)
        # obj就是那个对象
        # print(obj.pk)
        # print(obj.studio.sum_row

        return redirect('admin/')

    else:
        play_list = models.Play.objects.all()
        studio_list = models.Studio.objects.all()
        return render(requests, 'add_scheme.html', {'play_list': play_list, 'studio_list': studio_list})


def index(requests):
    return render(requests, 'index.html')


def show_plays(requests):
    play_list = models.Play.objects.all()
    return render(requests, 'show_plays.html', {'play_list': play_list})


def show_shemes(requests):
    play_idd = requests.GET.get("pk")
    schemes_list = models.Scheme.objects.filter(play_id=play_idd)
    # print(schemes_list)
    return render(requests, 'show_schemes.html', {'schemes_list': schemes_list})


def show_seats(requests):
    scheme_idd = requests.GET.get("sid")
    this_scheme = models.Scheme.objects.get(pk=scheme_idd)
    saled_tickets = models.Ticket.objects.filter(scheme_id=scheme_idd, state=1)
    # print(this_studio.sum_col,type(this_studio))
    # print(this_tickets)
    # print(saled_tickets)
    # print(type(saled_tickets.first().str_col))
    return render(requests, 'show_seats.html', {'this_scheme': this_scheme, 'saled_tickets': saled_tickets})


def show_ticket(requests):
    col = requests.GET.get("col")
    row = requests.GET.get("row")
    schemeId = requests.GET.get("sid")

    obj = models.Ticket.objects.create(col=col, row=row, scheme_id=schemeId, state=1)
    return render(requests, 'show_ticket.html', {'obj': obj})


def tic(requests):
    tic = models.Ticket.objects.filter(scheme__play_id='1')
    print(tic)
    return HttpResponse('test')


def addlotstic(request):
    for col in range(6, 9):
        for row in range(6, 9):
            schemeId = 19
            models.Ticket.objects.create(col=col, row=row, scheme_id=schemeId, state=1)

    return HttpResponse("ok")
