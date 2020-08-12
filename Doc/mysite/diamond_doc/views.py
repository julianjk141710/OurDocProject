import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import UserInfo
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def sayHello(request):
    return HttpResponse("hello world")

class UserMethod:

    @staticmethod
    def login_user(request):
        if request.method == "POST":
            data = json.loads(request.body)
            email = data.get("username")
            password = data.get("password")
            print("登陆")
            print(email)
            print(password)
            if email is not None and password is not None:
                islogin = authenticate(request, username=email, password=password)
                if islogin:
                    login(request, islogin)
                    return JsonResponse({
                        "status": 0,
                        "message": "Login Success",
                        "email": email
                    })
                else:
                    return JsonResponse({
                        "status": 1,
                        "message": "登录失败, 请检查用户名或者密码是否输入正确."
                    })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "参数错误"
                })


    # 注销
    @staticmethod
    def logout_user(request):
        logout(request)
        return JsonResponse({
            "status": 0
        })


    @staticmethod
    def register(request):
        if request.method == "POST":
            data = json.loads(request.body)

            if request.GET.get("select") is not None:
                print("select 是" + request.GET.get("select"))
                select_username = data.get("select_username")
                print(select_username)
                try:
                    User.objects.get(username=select_username)
                    return JsonResponse({
                        "status": 0,
                        "is_indb": 1
                    })
                except:
                    return JsonResponse({
                        'status': 0,
                        "is_indb": 0
                    })
            print("1111111")
            username = data.get("email")
            password = data.get("password")
            email = data.get("email")
            nickname = data.get("nickname")
            print(username)
            print(password)
            print(email)
            if username is not None and password is not None and email is not None:
                try:
                    user = User.objects.create_user(username=email, password=password, email=email)
                    user.save()
                    userInfo = UserInfo(user = user)
                    userInfo.user_nickname = nickname
                    userInfo.save()
                    login_user = authenticate(request, username=username, password=password)
                    if login_user:
                        login(request, login_user)
                        print("注册成功!!!!")
                        return JsonResponse({
                            "status": 0,

                            "message": "Register and Login Success"
                        })

                except:
                    return JsonResponse({
                        "status": 2,
                        "message": "注册失败, 该用户名已经存在."
                    })

        else:
            return JsonResponse({
                "status": 1,
                "message": "error method"
            })
