from django.db import models


class JiguiInfo(models.Model):
    #jifang_group = models.ForeignKey("index.JifangGroup", to_field='uid',default=1)  ##用户组表,默认id  user_group_id 数字
    #name= models.CharField(max_length=64,db_index=True)

    jq = models.CharField(max_length=64)
    zy = models.CharField(max_length=64)
    ziy = models.CharField(max_length=64)
    zs = models.CharField(max_length=64)
    zb = models.CharField(max_length=64)
    sh = models.CharField(max_length=64)
    xz = models.CharField(max_length=64)
    name = models.ForeignKey(to="index.JifangGroup",to_field='uid',db_index=True)
    d = models.ManyToManyField(to="dx")
    yong = models.CharField(max_length=64)
    ctime= models.DateTimeField(auto_now_add=True,null=True)
    utime = models.DateTimeField(auto_now=True, null=True)

class  dx(models.Model):
    xuan = models.CharField(max_length=64)







