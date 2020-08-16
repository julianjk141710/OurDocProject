import django.utils.timezone as timezone
import time
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userinfo')
    user_nickname = models.CharField(max_length = 16, null = True)
    user_icon = models.URLField(null = True)

class TeamInfo(models.Model):
    team_id = models.IntegerField(default = 0)
    team_manager = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    team_name = models.CharField(max_length = 16)
    team_description = models.CharField(max_length = 256)
    class Meta:
        unique_together = (("team_id"),)

class FileInformation(models.Model):
    file_id = models.IntegerField(default = 0)
    file_name = models.CharField(max_length = 64)
    file_founder = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
    file_foundTime = models.DateTimeField(auto_now_add = True)
    # file_lastBrowseTime = models.DateTimeField(default=timezone.now)
    file_lastModifiedTime = models.DateTimeField(auto_now = True)
    # file_doc = models.FileField(upload_to = 'word/')
    # file_size = models.IntegerField(default=0)
    file_text = models.TextField(default="")
    file_is_delete = models.SmallIntegerField(default=0)
    file_is_free = models.SmallIntegerField(default = 1)
    # file_teamBelong = models.ForeignKey(TeamInfo, on_delete = models.CASCADE, default = None)
    class Meta:
        unique_together = (("file_id"),)

class TeamFile(models.Model):
    file_info = models.ForeignKey(FileInformation, on_delete=models.CASCADE)
    team_info = models.ForeignKey(TeamInfo, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("file_info", "team_info"),)


class FileReview(models.Model):
    file_id = models.ForeignKey(FileInformation, on_delete = models.CASCADE)
    user_id = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
    review_text = models.CharField(max_length = 512)
    review_time = models.DateTimeField(auto_now_add = True)
    class Meta:
        unique_together = (("file_id"),)

class RecentBrowse(models.Model):
    file_id = models.ForeignKey(FileInformation, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    browse_time = models.DateTimeField(auto_now = True)
    class Meta:
        unique_together = (("user_id", "file_id"),)




class GeneralAuthority(models.Model):
    file_info = models.ForeignKey(FileInformation, on_delete=models.CASCADE)
    read_file = models.SmallIntegerField()
    write_file = models.SmallIntegerField()
    share_file = models.SmallIntegerField()
    review_file = models.SmallIntegerField()
    class Meta:
        unique_together = (("file_info"),)

class SpecificAuthority(models.Model):
    file_info = models.ForeignKey(FileInformation, on_delete=models.CASCADE)
    user_info = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
    read_file = models.SmallIntegerField()
    write_file = models.SmallIntegerField()
    share_file = models.SmallIntegerField()
    review_file = models.SmallIntegerField()
    class Meta:
        unique_together = (("user_info", "file_info"),)


class TeamUser(models.Model):
    team_info = models.ForeignKey(TeamInfo, on_delete= models.CASCADE)
    user_info = models.ForeignKey(UserInfo, on_delete= models.CASCADE)
    class Meta:
        unique_together = (("team_info", "user_info"),)

#
# class AdminInfo(models.Model):
#     admin_id = models.IntegerField(primary_key = True)
#     admin_account = models.CharField(max_length = 16)
#     admin_password = models.CharField(max_length = 16)
#     admin_nickname = models.CharField(max_length = 16)
#     admin_icon = models.URLField()



class Favorites(models.Model):
    favorite_id = models.IntegerField(default = 0)
    user_info = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
    file_info = models.ForeignKey(FileInformation, on_delete = models.CASCADE)
    class Meta:
        unique_together = (("user_info", "file_info","favorite_id"),)

class DocTemplates(models.Model):
    template_id = models.IntegerField(default = 0)
    template_text = models.TextField(default="")
    template_name = models.CharField(max_length=32)
    class Meta:
        unique_together = (("template_id"),)


class NotificationsInfo(models.Model):
    noti_id = models.IntegerField(default = 0)
    post_info = models.CharField(default="", max_length=64)
    receive_info = models.CharField(default="", max_length=64)
    notification_text = models.TextField(default="")
    post_time = models.DateTimeField(auto_now_add=True)
    is_new = models.SmallIntegerField(default=1)
    is_invitation = models.SmallIntegerField(default=0)
    class Meta:
        unique_together = (("noti_id", "post_info", "receive_info",),)




