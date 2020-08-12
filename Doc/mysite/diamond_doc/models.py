from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userinfo')
    user_nickname = models.CharField(max_length = 16, null = True)
    user_icon = models.URLField(null = True)

# class TeamInfo(models.Model):
#     team_id = models.IntegerField(primary_key=True)
#     team_name = models.CharField(max_length = 16)
#     team_description = models.CharField(max_length = 256)
#
# class TeamUser(models.Model):
#     team_id = models.ForeignKey(TeamInfo, on_delete= models.CASCADE)
#     user_id = models.ForeignKey(UserInfo, on_delete= models.CASCADE)
#     class Meta:
#         unique_together = (("team_id", "user_id"),)
#
#
# class FileInfo(models.Model):
#     file_id = models.IntegerField(primary_key=True)
#     file_name = models.CharField(max_length = 64)
#     file_founder = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
#     file_foundTime = models.DateTimeField(auto_now_add = True)
#     file_lastModifiedTime = models.DateTimeField(auto_now = True)
#     file_teamBelong = models.ForeignKey(TeamInfo, on_delete = models.CASCADE)
#
# class AdminInfo(models.Model):
#     admin_id = models.IntegerField(primary_key = True)
#     admin_account = models.CharField(max_length = 16)
#     admin_password = models.CharField(max_length = 16)
#     admin_nickname = models.CharField(max_length = 16)
#     admin_icon = models.URLField()

# class RecycleBin(models.Model):
#     file_id = models.ForeignKey(FileInfo, on_delete = models.CASCADE)
#     user_id = models.ForeignKey(UserInfo, on_delete= models.CASCADE)
#     origin_dir = models.URLField()
#     deleted_time = models.DateTimeField(auto_now_add = True)
#     class Meta:
#         unique_together = (("file_id", "user_id"),)

# class Favorites(models.Model):
#     favorite_id = models.IntegerField(primary_key = True)
#     user_id = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
#     file_num = models.IntegerField()
#     class Meta:
#         unique_together = (("user_id"),)
#
# class FavoritesFile(models.Model):
#     favorite_id = models.ForeignKey(Favorites, on_delete = models.CASCADE)
#     file_id = models.ForeignKey(FileInfo, on_delete = models.CASCADE)
#     class Meta:
#         unique_together = (("favorite_id", "file_id"),)
#
# class FileReview(models.Model):
#     file_id = models.ForeignKey(FileInfo, on_delete = models.CASCADE)
#     user_id = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
#     review_text = models.CharField(max_length = 512)
#     class Meta:
#         unique_together = (("file_id"),)
#
# class RecentBrowse(models.Model):
#     file_id = models.ForeignKey(FileInfo, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
#     browse_time = models.DateTimeField(auto_now = True)
#     class Meta:
#         unique_together = (("user_id", "file_id"),)
#
# class GeneralAuthority(models.Model):
#     file_id = models.ForeignKey(FileInfo, on_delete=models.CASCADE)
#     read_file = models.SmallIntegerField()
#     write_file = models.SmallIntegerField()
#     share_file = models.SmallIntegerField()
#     review_file = models.SmallIntegerField()
#     class Meta:
#         unique_together = (("file_id"),)
#
# class SpecificAuthority(models.Model):
#     file_id = models.ForeignKey(FileInfo, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
#     read_file = models.SmallIntegerField()
#     write_file = models.SmallIntegerField()
#     share_file = models.SmallIntegerField()
#     review_file = models.SmallIntegerField()
#     class Meta:
#         unique_together = (("user_id", "file_id"),)

