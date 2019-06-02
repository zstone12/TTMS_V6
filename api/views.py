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
            obj = models.User.objects.create(username=username, password=password,email=email)
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
        login=request.session.get('login')
        if login:
            return render(request, 'apitest.html')
        else:
            return HttpResponse('login')

#注销
class Logout(APIView):
    def get(self, request):
        try:
            del request.session['login']
        except KeyError:
            pass
        return HttpResponse("You're logged out.")

class Index(APIView):
    def get(self, request):
        login=request.session.get('login')
        if login:
            return render(request, 'indexindex.html')
        else:
            return HttpResponse('please login')