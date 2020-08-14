import json
import random
import time

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import UserInfo, FileInformation, FileReview, RecentBrowse, TeamInfo
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def sayHello(request):
    return HttpResponse("hello world")

#用于获取用户信息
#myInfo:true
def getInfo(request):
    if request.method == "POST":
        data = json.loads(request.body)
        show_myInfo = data.get("myInfo")

        if show_myInfo is not None and show_myInfo == "true":
            userInfo = UserInfo.objects.get(user = request.user)
            return JsonResponse({
                "status" : 0,
                "nickname" : userInfo.user_nickname,
                "password" : userInfo.user.password,
                "email" : userInfo.user.email
            })
        else :
            #
            return JsonResponse({
                "status" : 1,
                "message": "请求错误"
            })

class FileMethod:
    @staticmethod
    def hello(request):
        print()

    # #Headers key:content-type value:multipart/form-data
    # #body key:前端的变量名 value:参数值
    # @staticmethod
    # def getFile(request):
    #     if request.method == "POST":
    #         #获取前端传来的word文件 前端字段是word
    #         file_doc = request.FILES.get("word")
    #         file_name = request.POST.get("file_name")
    #         tmpUser = UserInfo.objects.get(user = request.user)
    #         fileInfo = FileInformation(file_founder = tmpUser, file_doc = file_doc,file_name = file_name, file_id = random.randint(10,20))
    #         fileInfo.save()
    #         return JsonResponse({
    #             "status":"0",
    #             "message":"文件上传成功"
    #         })
    #     else:
    #         return JsonResponse({
    #             "status":"1",
    #             "message":"文件上传失败"
    #         })

    #获取文件内容函数 后端会返回一个文件的全部信息 具体返回的参数如下，前端根据需要提取即可:
    # "file_text": retFile.file_text,
    # "file_name": retFile.file_name,
    # "file_founder": retFile.file_founder.user.email,
    # "file_is_delete": retFile.file_is_delete,
    # "file_is_free": retFile.file_is_free,
    # "file_found_time": retFile.file_foundTime,
    # "file_lastModifiedTime": retFile.file_lastModifiedTime

    #需要前端传递的参数
    #getFile:getFile 值不是这个的话不会返回文件相关信息
    #file_id:要获取的文档的id
    @staticmethod
    def getFile(request):
        if request.method == "POST":
            data = json.loads(request.body)
            getFile = data.get("getFile")
            if getFile is not None and getFile == "getFile":
                file_id = data.get("file_id")
                retFile = FileInformation.objects.filter(file_id = file_id).first()
                if retFile:
                    retFile.file_is_free = 0
                    return JsonResponse({
                        "status":0,
                        "file_text":retFile.file_text,
                        "file_name":retFile.file_name,
                        "file_founder":retFile.file_founder.user.email,
                        "file_is_delete":retFile.file_is_delete,
                        "file_is_free":retFile.file_is_free,
                        "file_found_time":retFile.file_foundTime,
                        "file_lastModifiedTime":retFile.file_lastModifiedTime
                    })
                else:
                    return JsonResponse({
                        "status":1,
                        "message":"该文档不存在"
                    })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "参数错误"
                })
        else:
            return JsonResponse({
                "status": 3,
                "message": "请求错误"
            })

    #用于分享文档 会返回文档id
    #shareFile:shareFile
    #file_id:文档id
    @staticmethod
    def shareFile(request):
        if request.method == "POST":
            data = json.loads(request.body)
            shareFile = data.get("shareFile")
            if shareFile is not None and shareFile == "shareFile":
                file_id = data.get("file_id")
                retFile = FileInformation.objects.filter(file_id = file_id).first()
                if retFile and retFile.file_is_delete == 0:
                    return JsonResponse({
                        "status" : 0,
                        "file_id" : file_id
                    })
                else :
                    return JsonResponse({
                        "status": 1,
                        "message": "要的分享文档不存在"
                    })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "参数错误"
                })
        else:
            return JsonResponse({
                "status": 3,
                "message": "请求错误"
            })


    #用于申请编辑文档 如果当前没人占用此文档 就会返回该文档的全部信息（数据库里存储的有关本文档的全部内容）
    #editFile:editFile
    #file_id:file_id
    @staticmethod
    def applyEditFile(request):
        if request.method == "POST":
            data = json.loads(request.body)
            editFile = data.get("editFile")
            if editFile is not None and editFile == "editFile":
                file_id = data.get("file_id")
                retFile = FileInformation.objects.filter(file_id=file_id).first()
                print(retFile.file_is_free)
                if retFile:
                    if retFile.file_is_free == 1 and retFile.file_is_delete == 0:
                        retFile.file_is_free = 0
                        retFile.save()
                        return JsonResponse({
                            "status": 0,
                            "file_text": retFile.file_text,
                            "file_name": retFile.file_name,
                            "file_founder": retFile.file_founder.user.email,
                            "file_is_delete": retFile.file_is_delete,
                            "file_is_free": retFile.file_is_free,
                            "file_found_time": retFile.file_foundTime,
                            "file_lastModifiedTime": retFile.file_lastModifiedTime
                        })
                    else:
                        return JsonResponse({
                            "status" : 1,
                            "message" : "请求的文档正在被他人编辑或已被删除"
                        })
                else:
                    return JsonResponse({
                        "status": 2,
                        "message": "文档不存在"
                    })
            else:
                return JsonResponse({
                    "status": 3,
                    "message": "参数错误"
                })
        else:
            return JsonResponse({
                "status": 4,
                "message": "请求错误"
            })


    #用于上传更新过的富文本 如果是修改富文本内容一定要调用这个函数！！！！！！！！！！
    #postFile:postFile
    #file_id:file_id
    #newContent:更新后的富文本内容
    #newName:更新后的文档名字 即使没改名字也要给后端
    @staticmethod
    def postModifiedFile(request):
        if request.method == "POST":
            data = json.loads(request.body)
            postFile = data.get("postFile")
            if postFile is not None and postFile == "postFile":
                file_id = data.get("file_id")
                fileInfo = FileInformation.objects.filter(file_id = file_id).first()
                if fileInfo:
                    newContent = data.get("newContent")
                    newName = data.get("newName")
                    fileInfo.file_text = newContent
                    fileInfo.file_name = newName
                    fileInfo.file_is_free = 1
                    fileInfo.save()
                    return JsonResponse({
                        "status" : 0,
                        "message" : "更新文档成功"
                    })
                else:
                    return JsonResponse({
                        "status": 1,
                        "message": "要更改的文档不存在"
                    })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "参数错误"
                })
        else:
            return JsonResponse({
                "status": 3,
                "message": "请求错误"
            })


    #最近浏览
    #recent:recent
    @staticmethod
    def recentBrowse(request):
        if request.method == "POST":
            data = json.loads(request.body)
            recent = data.get("recent")
            if recent is not None and recent == "recent":
                tmpUser = request.user
                userInfo = UserInfo.objects.get(user = tmpUser)
                recentFiles = RecentBrowse.objects.filter(user_id = userInfo).order_by("browse_time")
                recentFilesList = list(recentFiles)
                retNameList = []
                retTimeList = []
                cnt = 0
                for i in recentFilesList:
                    if i.file_id.file_is_delete != 1:
                        retNameList.append(i.file_id.file_name)
                        retTimeList.append(i.browse_time)
                        cnt += 1
                return JsonResponse({
                    "status":1,
                    # "list":recentFilesList
                    "namelist":retNameList,
                    "timelist":retTimeList,
                    "message":"已经返回最近浏览的文件名字列表"
                })
            else:
                return JsonResponse({
                    "status":2,
                    "message":"请求参数错误"
                })
        return JsonResponse({
            "status": 3,
            "message": "请求方法错误"
        })


    #用于上传全新的富文本
    @staticmethod
    def uploadFileText(request):
        #需要的前端参数
        #upload:是否上传 如果参数值是upload就表明请求上传
        #content：富文本信息
        #file_name:文件名字
        print("1111111")
        if request.method == "POST":
            print("文本函数")
            data = json.loads(request.body)
            upload = data.get("upload")
            if upload == "upload":
                content = data.get("content")
                if content is not None:
                    tmpUser = request.user
                    file_name = data.get("file_name")
                    userInfo = UserInfo.objects.get(user = tmpUser)
                    fileInfo = FileInformation(file_text = content, file_founder = userInfo, file_is_free = 1, file_is_delete = 0,
                                               file_name = file_name, file_id = int(str(time.time()).split('.')[0]))
                    fileInfo.save()
                    return JsonResponse({
                        "status":0,
                        "message":"富文本上传成功"
                    })
                else:
                    return JsonResponse({
                        "status": 1,
                        "message": "富文本无内容"
                    })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "非上传请求"
                })
        else :
            return JsonResponse({
                "status": 3,
                "message": "请求方式错误"
            })

    #用于判断文档是否处于可编辑状态
    @staticmethod
    def getFileEditStatus(request):
        #需要前端传递的参数:
        #freeFile:这个参数的值是freeOrNot时 会认为是在请求查看文档是否处于free状态
        #file_id:文档id

        if request.method == "POST":
            data = json.loads(request.body)
            freeFile = data.get("freeFile")
            if freeFile is not None and freeFile == "freeOrNot":
                file_id = data.get("file_id")
                tmpFile = FileInformation.objects.filter(file_id = file_id).first()
                if tmpFile:
                    if tmpFile.file_is_free == 1:
                        return JsonResponse({
                            "status":0,
                            "message":"可以编辑"
                        })
                    else:
                        return JsonResponse({
                            "status":1,
                            "message":"不可编辑"
                        })
                else:
                    return JsonResponse({
                        "status": 2,
                        "message": "文件不存在"
                    })
            else:
                return JsonResponse({
                    "status": 3,
                    "message": "参数错误"
                })
        else:
            return JsonResponse({
                "status": 4,
                "message": "请求方法错误"
            })

    @staticmethod
    # 将文件移动到回收站
    #delete_file:delete_file
    #file_id:需要回复的文档id
    def moveto_recyclebin(request):
        if request.method == "POST":
            data = json.loads(request.body)
            delete_file = data.get("delete_file")
            if delete_file is not None and delete_file == "delete_file":
                fileInfo = FileInformation.objects.filter(file_id=data.get("file_id")).first()
                if fileInfo and fileInfo.file_is_delete == 0:
                    fileInfo.file_is_delete = 1
                    fileInfo.save()
                    return JsonResponse({
                        "status": 0,
                        "data": "删除成功"
                    })
                else:
                    return JsonResponse({
                        "status": 1,
                        "message": "该文件不存在或已经被删除"
                    })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "参数错误"
                })
        else:
            return JsonResponse({
                "status": 3,
                "message": "请求错误"
            })

    @staticmethod
    # 从回收站回复
    #recover_file:recover_file
    #file_id:需要回复的文档id
    def recoverfrom_recyclebin(request):
        if request.method == "POST":
            data = json.loads(request.body)
            recover_file = data.get("recover_file")
            if recover_file is not None and recover_file == "recover_file":
                fileInfo = FileInformation.objects.filter(file_id=data.get("file_id")).first()
                if fileInfo and fileInfo.file_is_delete == 1:
                    fileInfo.file_is_delete = 0
                    fileInfo.save()
                    return JsonResponse({
                        "status": 0,
                        "data": "恢复成功"
                    })
                else:
                    return JsonResponse({
                        "status": 1,
                        "message": "该文件不存在或已经被恢复"
                    })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "参数错误"
                })
        else:
            return JsonResponse({
                "status": 3,
                "message": "请求错误"
            })


class UserMethod:
    @staticmethod
    def get_status(request):
        if request.user.is_authenticated:
            return JsonResponse({
                "status": 0,
                "username": str(request.user),
                "email": str(request.user.email),
            })
        else:
            return JsonResponse({
                "status": 1
            })

    @staticmethod
    def login_user(request):
        if request.method == "POST":
            data = json.loads(request.body)
            email = data.get("email")
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
        return JsonResponse({
            "status": 3,
            "message": "请求错误"
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
                    print("except")
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

    @staticmethod
    def modify_nickname(request):
        if request.method == "POST":
            data = json.loads(request.body)
            new_nickname = data.get("nickname")

            if len(new_nickname) == 0:
                #昵称为空返回status和message
                return JsonResponse({
                    "status" : 0,
                    "message" : "新昵称不可为空"
                })
            elif len(new_nickname) > 16 :
                #昵称长度大于16返回status和message
                return JsonResponse({
                    "status": 0,
                    "message": "新昵称过长"
                })
            else :
                userInfo = UserInfo.objects.get(user = request.user)
                userInfo.user_nickname = new_nickname
                userInfo.save()
                print(userInfo.user.email)
                print(userInfo.user_nickname)
                #修改成功返回status、message、以及修改后的新昵称new_nickname
                return JsonResponse({
                    "status" : 1,
                    "message" : "昵称修改成功",
                    "new_nickname" : new_nickname
                })




#用于给文档添加评论
#add_review:add_review
#review_text:评论内容
#file_id:文档id
def add_review(request):
    if request.method == "POST":
        data = json.loads(request.body)
        add_review = data.get("add_review")
        # 添加评论
        if add_review is not None and add_review == "add_review":
            # 将json转换为python dict格式
            if data.get("review_text") is not None:
                # try:
                fileInfo = FileInformation.objects.filter(file_id=data.get("file_id")).first()
                userInfo = UserInfo.objects.get(user = request.user)
                db = FileReview(review_text=data.get("review_text"), user_id=userInfo,file_id=fileInfo)
                db.save()
                return JsonResponse({
                    "status_code": 0,
                    "data": "success"
                })
            else:
                return JsonResponse({
                    "status_code": 1,
                    "error": "text is none"
                })
        else:
            return JsonResponse({
                "status": 2,
                "message": "add_review is none"
            })
    else:
        return JsonResponse({
            "status": 3,
            "message": "error method"
        })




#创建团队
def create_team(request):
    if request.method == "POST":
        data = json.loads(request.body)
        create = data.get("create")
        if create is not None and create=="create":
            # 将json转换为python dict格式
            # try:
            tmpUser = request.user
            userInfo = UserInfo.objects.filter(user = tmpUser).first()
            team_description = data.get("team_description")
            team_name = data.get("team_name")
            db = TeamInfo(team_name=team_name, team_manager=userInfo, team_description=team_description)
            db.save()
            return JsonResponse({
                "status_code": 0,
                "data": "create success"
            })
        else:
            return JsonResponse({
                "status": 1,
                "message": "create is none"
            })
    else:
        return JsonResponse({
            "status": 2,
            "message": "error method"
        })