from django.shortcuts import render, HttpResponse
from app01 import models
from rest_framework.views import APIView
from app01.serializers import *
from rest_framework.response import Response


# Create your views here.

class BaseResponse(object):
    def __init__(self):
        self.code = 1000
        self.msg = ""
        self.data = None

    @property
    def dict(self):
        return self.__dict__


# 注册
class Reg(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        username = receive.get('username')
        password = receive.get('password')
        re_password = receive.get('re_password')
        email = receive.get('email')
        if password == re_password:
            obj = models.User.objects.create(username=username, password=password, email=email)
            response.msg = '注册成功'
            response.code = 2000
        else:
            response.msg = '注册失败'
            response.code = 2001
        return Response(response.dict)


# 登录
class Login(APIView):
    def post(self, request):
        response = BaseResponse()
        receive = request.data
        username = receive.get('username')
        password = receive.get('password')
        user = models.User.objects.filter(username=username, password=password)
        if user:
            request.session['login'] = True
            response.msg = "登陆成功"
            response.data = username
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
        image = receive.get('image')
        try:
            models.Play.objects.create(name=name,
                                       brief_info=brief_info,
                                       play_length=play_length,
                                       price=price,
                                       image=image, )
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
        image = receive.get('image')
        print(id, name, brief_info, play_length, price, image)
        try:
            obj = models.Play.objects.get(id=id)
            print(obj.name)
            obj.name = name
            obj.brief_info = brief_info
            obj.play_length = play_length
            obj.price = price
            obj.image = image
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
            models.Scheme.objects.filter(pk=id).delete()
            response.msg = "删除成功"
        except Exception as e:
            response.msg = "删除失败"
        return Response(response.dict)
