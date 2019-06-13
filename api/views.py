from django.shortcuts import render, HttpResponse
from app01 import models
from rest_framework.views import APIView
from app01.serializers import *
from rest_framework.response import Response
import json


# from django.forms.models import model_to_dic


# Create your views here.

class BaseResponse(object):
    def __init__(self):
        self.code = 1000
        self.msg = ""
        self.data = None

    @property
    def dict(self):
        return self.__dict__


class IS_login(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        session_key = receive.get('session_id')
        response.data = {}
        if request.session.exists(session_key):
            response.code = '200'
            response.data['is_login'] = True
            return Response(response.dict)

        else:
            response.msg = '未登录'
            response.data['is_login'] = False
            return Response(response.dict)


# 注册
class Reg(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        print(receive)
        username = receive.get('username')
        password = receive.get('password')
        re_password = receive.get('re_password')
        email = receive.get('email')
        user = models.User.objects.filter(username=username)
        if user:  # 存在这个用户名的用户
            response.msg = '已存在该用户'
            response.code = '2002'
        else:
            if password == re_password:
                obj = models.User.objects.create(username=username, password=password, email=email)
                response.msg = '注册成功'
                response.code = 2000
            else:
                response.msg = '两次密码不同'
                response.code = 2001

        return Response(response.dict)


# 登录
class Login(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        # print(request.GET)
        # json.loads(request.body.decode())
        #
        username = receive.get('username')
        password = receive.get('password')
        # print(request.GET.get('username'))
        print(request.data)
        # print(username,password)
        user = models.User.objects.filter(username=username, password=password).first()
        if user:
            if not request.session.session_key:
                request.session.create()
            session_id = request.session.session_key
            request.session['login'] = True
            response.data = {}
            response.data['session_id'] = session_id
            response.data['name'] = username
            response.data['user_id'] = user.id
            response.data['user_email'] = user.email
            response.msg = "登陆成功"
        else:
            try:
                models.User.objects.get(username=username)
                response.msg = "密码错误!"
                response.code = 1002
            except BaseException:
                response.msg = "用户不存在!"
                response.code = 1003
        return Response(response.dict)


class test(APIView):
    def get(self, request):
        return render(request, 'apitest.html')


# 注销
class Logout(APIView):
    def get(self, request):
        response = BaseResponse()
        try:
            del request.session['login']
        except KeyError:
            pass
        return Response(response.dict)


class Index(APIView):
    def get(self, request):
        login = request.session.get('login')
        if login:
            return render(request, 'indexindex.html')
        else:
            return HttpResponse('please login')


class GetPlay(APIView):
    def get(self, request):
        plays = models.Play.objects.all()
        plays_obj = PlaySerializer(plays, many=True)
        return Response(plays_obj.data)

    def post(self, request):
        receive = request.data
        pk = receive.get('id')
        play = models.Play.objects.filter(pk=pk)
        plays_obj = PlaySerializer(play, many=True)
        return Response(plays_obj.data)


class AddPlay(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        name = receive.get('name')
        brief_info = receive.get('brief_info')
        play_length = receive.get('play_length')
        price = receive.get('price')
        director = receive.get('director')
        actor = receive.get('actor')
        play_type = receive.get('play_type')

        print(name, brief_info, play_length, price, director, actor,
              play_type)
        try:
            models.Play.objects.create(name=name,
                                       brief_info=brief_info,
                                       play_length=play_length,
                                       price=price,

                                       director=director,
                                       actor=actor,
                                       play_type=play_type,
                                       )
            response.msg = "新增成功"
        except Exception as e:
            response.msg = "新增失败"
        return Response(response.dict)


class DelPlay(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        id = receive.get('id')
        try:
            models.Play.objects.filter(pk=id).delete()
            response.msg = "删除成功"
        except Exception as e:
            response.msg = "删除失败"
        return Response(response.dict)


class UpdatePlay(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        id = receive.get('id')
        name = receive.get('name')
        brief_info = receive.get('brief_info')
        play_length = receive.get('play_length')
        price = receive.get('price')
        director = receive.get('director')
        actor = receive.get('actor')
        play_type = receive.get('play_type')

        # print(id, name, brief_info, play_length, price, image)
        try:
            obj = models.Play.objects.get(id=id)
            print(obj.name)
            obj.name = name
            obj.brief_info = brief_info
            obj.play_length = play_length
            obj.price = price
            obj.director = director
            obj.actor = actor
            obj.play_type = play_type
            obj.save()
            response.msg = "修改成功"
        except Exception as e:
            response.msg = "修改失败"
        return Response(response.dict)


class GetScheme(APIView):
    def get(self, request):
        schemes = models.Scheme.objects.all()
        schemes_obj = SchemeSerializer(schemes, many=True)
        return Response(schemes_obj.data)

    def post(self, request):
        receive = request.data
        pk = receive.get('sch_id')
        scheme = models.Scheme.objects.filter(pk=pk)
        schemes_obj = SchemeSerializer(scheme, many=True)
        return Response(schemes_obj.data)


class AddScheme(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data

        start_time = receive.get('start_time')
        play = receive.get('play_id')
        studio = receive.get('stu_id')
        print(start_time, play, studio)
        try:
            models.Scheme.objects.create(
                start_time=start_time,
                play_id=play,
                studio_id=studio,
            )
            response.msg = "新增成功"
        except Exception as e:
            response.msg = "新增失败"
        return Response(response.dict)


class UpdateScheme(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        start_time = receive.get('start_time')
        play = receive.get('play_id')
        studio = receive.get('stu_id')
        id = receive.get('id')

        try:
            obj = models.Scheme.objects.get(id=id)
            obj.start_time = start_time
            obj.play_id = play
            obj.studio_id = studio
            obj.save()
            response.msg = "修改成功"
        except Exception as e:
            response.msg = "修改失败"
        return Response(response.dict)


class DelScheme(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        id = receive.get('id')
        try:
            models.Scheme.objects.filter(id=id).delete()
            response.msg = "删除成功"
        except Exception as e:
            response.msg = "删除失败"
        return Response(response.dict)


class GetStudio(APIView):
    def get(self, request):
        studios = models.Studio.objects.all()
        studios_obj = StudioSerializer(studios, many=True)
        return Response(studios_obj.data)

    def post(self, request):
        receive = request.data
        pk = receive.get('stu_id')
        studio = models.Studio.objects.filter(pk=pk)
        studios_obj = StudioSerializer(studio, many=True)
        return Response(studios_obj.data)


class AddStudio(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data

        sum_row = receive.get('sum_row')
        sum_col = receive.get('sum_col')
        # print(start_time, play, studio)
        print(sum_row, sum_col)
        try:
            models.Studio.objects.create(
                sum_row=sum_row,
                sum_col=sum_col,
            )
            response.msg = "新增成功"
        except Exception as e:
            response.msg = "新增失败"
        return Response(response.dict)


class UpdateStudio(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        sum_row = receive.get('sum_row')
        sum_col = receive.get('sum_col')
        id = receive.get('stu_id')

        try:
            obj = models.Studio.objects.get(id=id)
            obj.sum_row = sum_row
            obj.sum_col = sum_col
            obj.save()
            response.msg = "修改成功"
        except Exception as e:
            response.msg = "修改失败"
        return Response(response.dict)


class DelStudio(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        id = receive.get('stu_id')
        try:
            models.Studio.objects.filter(pk=id).delete()
            response.msg = "删除成功"
        except Exception as e:
            response.msg = "删除失败"
        return Response(response.dict)


class GetTicket(APIView):
    def get(self, request):
        tickets = models.Ticket.objects.all()
        response = BaseResponse()
        list_a = []
        data = {}
        for tic in tickets:
            data['ticid'] = tic.id
            data['name'] = tic.scheme.play.name
            data['time'] = tic.sale_time
            data['studio'] = tic.scheme.studio_id
            data['play_type'] = tic.scheme.play.play_type
            data['price'] = tic.scheme.play.price
            list_a.append(data)
            data = {}
        # tickets_obj = TicketSerializer(tickets, many=True)
        return Response(list_a)

    def post(self, request):
        receive = request.data
        pk = receive.get('tic_id')
        tic = models.Ticket.objects.filter(pk=pk).first()
        data = {}
        data['ticid'] = tic.id
        data['name'] = tic.scheme.play.name
        data['time'] = tic.sale_time
        data['studio'] = tic.scheme.studio_id
        data['play_type'] = tic.scheme.play.play_type
        data['price'] = tic.scheme.play.price

        return Response(data)


class AddTicket(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data

        sch_id = receive.get('sch_id')
        col = receive.get('col')
        row = receive.get('row')
        state = receive.get('state')
        sale_time = receive.get('sale_time')
        # print(start_time,play, studio)
        # print(sum_row, sum_col)
        print(sch_id, col, row, state, sale_time)
        try:
            models.Ticket.objects.create(
                scheme_id=sch_id,
                col=col,
                row=row,
                state=state,
                sale_time=sale_time,
            )
            response.msg = "新增成功"
        except Exception as e:
            response.msg = "新增失败"
        return Response(response.dict)


class UpdateTicket(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data

        id = receive.get('tic_id')
        sch_id = receive.get('sch_id')
        col = receive.get('col')
        row = receive.get('row')
        state = receive.get('state')
        sale_time = receive.get('sale_time')

        print(id, sch_id, col, row, state, sale_time)
        try:
            obj = models.Ticket.objects.get(id=id)
            obj.sch_id = sch_id
            obj.col = col
            obj.row = row
            obj.state = state
            obj.sale_time = sale_time
            obj.save()
            response.msg = "修改成功"
        except Exception as e:
            response.msg = "修改失败"
        return Response(response.dict)


class DelTicket(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        id = receive.get('tic_id')
        try:
            models.Ticket.objects.filter(pk=id).delete()
            response.msg = "删除成功"
        except Exception as e:
            response.msg = "删除失败"
        return Response(response.dict)


class GetPic(APIView):
    def get(self, request):
        data = ['http://129.204.185.247:8000/media/lun/1.jpg',
                'http://129.204.185.247:8000/media/lun/2.jpg',
                'http://129.204.185.247:8000/media/lun/3.jpg', ]
        return Response(data)


class GetSaleTic(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        scheme_id = receive.get('scheme_id')
        saled_tic = models.Ticket.objects.filter(scheme_id=scheme_id)
        ticket_obj = TicketSerializer(saled_tic, many=True)
        return Response(ticket_obj)


class GetUserTic(APIView):
    def post(self, request):
        receive = request.data
        user_id = receive.get('user_id')
        UserTic = models.Ticket.objects.filter(user=user_id)
        list_b = []
        data = {}

        for tic in UserTic:
            # 剧目名称、演出厅、开始时间、座位、票价、
            data['play_name']= tic.scheme.play.name
            data['studio'] = tic.scheme.studio.id
            data['studio'] = tic.scheme.start_time
            data['row'] = tic.row
            data['col'] = tic.col
            data['price'] = tic.scheme.play.price
            list_b.append(data)
            data = {}
        # tickets_obj = TicketSerializer(tickets, many=True)
        return Response(list_b)


class GetONplay(APIView):
    def get(self, request):
        on_play = models.Play.objects.filter(shangyin=1)
        onPlay = PlaySerializer(on_play, many=True)
        return Response(onPlay.data)


class GetNotplay(APIView):
    def get(self, request):
        noton_play = models.Play.objects.filter(shangyin=0)
        notonPlay = PlaySerializer(noton_play, many=True)
        return Response(notonPlay.data)


class GetshemeByplayID(APIView):
    def post(self, request):
        # schemeid
        # 放映时间
        # 类型
        # 放映厅
        # 座位情况(已售/总座位)
        # 价格
        receive = request.data
        play_id = receive.get('play_id')
        this_scheme = models.Scheme.objects.filter(play_id=play_id)
        list_b = []
        data = {}

        for sch in this_scheme:
            data['sch_id'] = sch.id
            # print(sch.id)
            data['start_time'] = sch.start_time
            data['play_type'] = sch.play.play_type
            data['studio'] = sch.studio_id
            data['price'] = sch.play.price
            saled_ticket = models.Ticket.objects.filter(scheme_id=sch.id, state=1).count()
            sum_ticket = sch.studio.sum_col * sch.studio.sum_row
            data['seat_ticket_count'] = saled_ticket
            data['sum_ticket_count'] = sum_ticket
            list_b.append(data)
            data = {}
        # tickets_obj = TicketSerializer(tickets, many=True)
        return Response(list_b)


class GetTicketBySchemeID(APIView):
    def post(self, request):
        receive = request.data
        scheme_id = receive.get('sch_id')
        saled_ticket = models.Ticket.objects.filter(scheme_id=scheme_id, state=1)
        saled_tickets = TicketSerializer(saled_ticket, many=True)
        return Response(saled_tickets.data)


class GetTicketinfo(APIView):
    def post(self, request):
        receive = request.data
        response = BaseResponse()
        response.msg = 'OK'
        sch_id = receive.get('sch_id')
        selectTicket = receive.get('selectTicket')
        user_id = receive.get('user_id')
        try:
            for tic in selectTicket:
                row = tic['row']
                col = tic['col']
                models.Ticket.objects.create(
                    scheme_id=sch_id,
                    col=col,
                    row=row,
                    state=1,
                    user_id=user_id
                )

            response.msg = "购票成功"
            response.code = 1002

        except BaseException:
            response.msg = "购票失败"
            response.code = 1003

        return Response(response.dict)
