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
    path('apis/user/logout', views.UserMethod.logout_user),#对应峥的退出登陆按钮
    # path('apis/user/file', views.FileMethod.getFile),#文件上传视图
    path('apis/user/recentBrowse', views.FileMethod.recentBrowse),#最近浏览视图
    path('apis/user/createDoc', views.FileMethod.uploadFileText),#最近浏览视图
    path('apis/user/fileReview', views.add_review),#添加文件评论视图
    path('apis/user/fileEditStatus', views.FileMethod.getFileEditStatus),#检测文档是否可以编辑
    path('apis/user/applyEditFile', views.FileMethod.applyEditFile),#申请编辑富文本

    #用于上传更新过的富文本 如果是修改富文本内容一定要调用这个函数！！！！！！！！！！
    #用于上传更新过的富文本 如果是修改富文本内容一定要调用这个函数！！！！！！！！！！
    #用于上传更新过的富文本 如果是修改富文本内容一定要调用这个函数！！！！！！！！！！
    path('apis/user/postModifiedFile', views.FileMethod.postModifiedFile),  # 更改文档内容

    path('apis/user/moveto_recyclebin', views.FileMethod.moveto_recyclebin),  # 申请编辑文档
    path('apis/user/recoverfrom_recyclebin', views.FileMethod.recoverfrom_recyclebin),  # 申请编辑文档
    path('apis/user/shareFile', views.FileMethod.shareFile),  # 分享文档
    path('apis/user/create_team', views.create_team)

]