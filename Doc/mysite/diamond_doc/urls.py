from django.urls import path

from . import views

urlpatterns = [
    # path('', views.sayHello),
    path('diamond/user/login', views.UserMethod.login_user),  # 登录
    path('diamond/user/logout', views.UserMethod.logout_user),  # 注销
    path('diamond/user/register', views.UserMethod.register),  # 注册
]