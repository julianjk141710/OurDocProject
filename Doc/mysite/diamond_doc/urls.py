from django.urls import path

from . import views

urlpatterns = [
    # path('', views.sayHello),
    path('apis/user/login', views.UserMethod.login_user),  # 登录
    path('apis/user/logout', views.UserMethod.logout_user),  # 注销
    path('apis/user/register', views.UserMethod.register),  # 注册
]