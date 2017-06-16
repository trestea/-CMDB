from django.db import models
# Create your models here.

class UserInfo(models.Model):
    ##id 列 自增,主键
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=64)
 #   user_group = models.ForeignKey("UserGroup", to_field='uid', default=1)  ##用户组表,默认id  user_group_id 数字
#    jifang = models.ForeignKey("JifangGroup",to_field='uid',unique=True)


class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)


class JifangGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    jifang = models.CharField(max_length=32)


class Quyu(models.Model):
    uid = models.AutoField(primary_key=True)
    quyu = models.CharField(max_length=32)
