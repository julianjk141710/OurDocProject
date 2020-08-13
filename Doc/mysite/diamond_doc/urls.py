from django.urls import path

from . import views

urlpatterns = [
    # path('', views.sayHello),
    path('apis/user/login', views.UserMethod.login_user),  # 登录
    path('apis/user/logout', views.UserMethod.logout_user),  # 注销
    path('apis/user/register', views.UserMethod.register),  # 注册
    path('apis/user/getstatus', views.UserMethod.get_status),  # 检查用户的登录状态
    path('apis/user/getInfo', views.getInfo), #对应峥的User.vue 获取用户的昵称 密码 邮箱
    path('apis/user/modify_nickname', views.UserMethod.modify_nickname),#对应峥的User.vue页面的修改昵称
    path('path/user/logout', views.UserMethod.logout_user)#对应峥的退出登陆按钮
]