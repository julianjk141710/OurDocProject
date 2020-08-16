from django.urls import path

from . import views

urlpatterns = [
    # path('', views.sayHello),
    path('apis/user/login', views.UserMethod.login_user),  # 登录
    path('apis/user/logout', views.UserMethod.logout_user),  # 注销
    path('apis/user/register', views.UserMethod.register),  # 注册
    path('apis/user/getstatus', views.UserMethod.get_status),  # 检查用户的登录状态
    path('apis/user/getInfo', views.getInfo), #获取用户的昵称 密码 邮箱
    path('apis/user/modify_nickname', views.UserMethod.modify_nickname),#修改昵称
    path('apis/user/logout', views.UserMethod.logout_user),#退出登陆

    path('apis/user/recentBrowse', views.FileMethod.recentBrowse),#最近浏览视图
    path('apis/user/createDoc', views.FileMethod.uploadFileText),#生成新的文档
    path('apis/user/fileReview', views.add_review),#添加文件评论视图
    path('apis/user/fileEditStatus', views.FileMethod.getFileEditStatus),#检测文档是否可以编辑
    path('apis/user/applyEditFile', views.FileMethod.applyEditFile),#申请编辑富文本

    #用于上传更新过的富文本 如果是修改富文本内容一定要调用这个函数！！！！！！！！！！
    #用于上传更新过的富文本 如果是修改富文本内容一定要调用这个函数！！！！！！！！！！
    #用于上传更新过的富文本 如果是修改富文本内容一定要调用这个函数！！！！！！！！！！
    path('apis/user/postModifiedFile', views.FileMethod.postModifiedFile),  # 更改文档内容

    path('apis/user/moveto_recyclebin', views.FileMethod.moveto_recyclebin),  # 删除文档
    path('apis/user/recoverfrom_recyclebin', views.FileMethod.recoverfrom_recyclebin),  # 恢复文档
    path('apis/user/shareFile', views.FileMethod.shareFile),  # 分享文档
    path('apis/user/create_team', views.create_team), #建立团队
    path('apis/user/checkGeneralAuthority', views.FileMethod.checkGeneralAuthority), #检查文档的通用权限
    path('apis/user/checkSpecificAuthority', views.FileMethod.checkSpecificAuthority), #检查文档的特定权限
    path('apis/user/setGeneralAuthority', views.FileMethod.setGeneralAuthority), #设定文档的通用权限
    path('apis/user/setSpecificAuthority', views.FileMethod.setSpecificAuthority), #设定文档的特定权限
    path('apis/user/add_favorite', views.add_favorite), #添加收藏
    path('apis/user/delete_favorite', views.delete_favorite), #删除收藏
    path('apis/user/my_favorite', views.my_favorite), #获取收藏的文档id和名字
    # path('apis/user/file', views.FileMethod.getFile),#文件上传视图
    # path('apis/user/add_teammate', views.add_teammate), #添加团队成员
    path('apis/user/delete_teammate', views.delete_teammate), #删除团队成员
    path('apis/user/myFile', views.FileMethod.myFile), #获取我的文档
    path('apis/user/myTeam', views.myTeam), #获取我参加的团队 包括创建的和加入的
    path('apis/user/addFileToTeam', views.FileMethod.addFileToTeam), #将文档添加到团队
    path('apis/user/deleteFileFromTeam', views.FileMethod.deleteFileFromTeam), #将文档从团队删除
    path('apis/user/showTeamFile', views.FileMethod.showTeamFile), #展示团队文档
    path('apis/user/test', views.test), #展示团队文档
    path('apis/user/delete_file', views.delete_file), #彻底删除文档
    path('apis/user/recyclebin_file', views.recyclebin_file),  # 展示回收站文档
    path('apis/user/showTemplates', views.showTemplates),  # 展示模版文档
    path('apis/user/postMessage', views.postMessage),  # 发送站内信
    path('apis/user/myNotifications', views.myNotifications),  # 展示我的站内信
    path('apis/user/hasRead', views.hasRead),  # 将站内信标示为已读
    path('apis/user/send_invitation', views.send_invitation),  # 发送团队邀请
    path('apis/user/addinto_team', views.addinto_team),#同意加入队伍
    # path('apis/user/bonjour', views.bonjour) #删除收藏
]