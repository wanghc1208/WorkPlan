# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class User(models.Model):
    name = models.CharField(max_length=128, unique=True,verbose_name='用户名')
    password = models.CharField(max_length=256,verbose_name="密码")
    # group = models.ForeignKey(to="Group", on_delete=models.CASCADE, verbose_name="所属小组")
    group = models.CharField(max_length=128, unique=True,verbose_name='所属小组')
    addTime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    # modifyTime = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")

    def __str__(self):
        return  self.name
    class Meta:
        db_table = "User"
        verbose_name="用户表"
        verbose_name_plural = verbose_name

class Group(models.Model):
    #小组表
    groupName = models.CharField(max_length=100,verbose_name="小组名称")
    addTime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")


    def __str__(self):
        return  self.groupName
    class Meta:
        db_table = "Group"
        verbose_name="小组表"
        verbose_name_plural = verbose_name

class PlanType(models.Model):
    # 计划类型表
    planId = models.AutoField(primary_key=True, verbose_name="小组ID")
    typeName = models.CharField(max_length=128,unique=True,verbose_name="计划名称")
    addTime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.typeName

    class Meta:
        db_table = "PlanType"
        verbose_name = "计划类型表"
        verbose_name_plural = verbose_name

class PlanDate(models.Model):
    #计划表时间表
    uname = models.ForeignKey(to="User",on_delete=models.CASCADE,verbose_name="用户")
    planTime = models.DateField(verbose_name="计划时间")
    # planName = models.CharField(max_length=128, unique=True,verbose_name="计划内容")
    # addTime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    # modifyTime = models.DateTimeField(auto_now=True,verbose_name="更新时间")


    def __str__(self):
        return  '%s' %(self.planTime)
    class Meta:
        db_table = "PlanDate"
        verbose_name="计划表时间表"
        verbose_name_plural = verbose_name

class Plan(models.Model):
    #计划表
    planTime = models.ForeignKey(to="PlanDate",on_delete=models.CASCADE,verbose_name="计划时间")
    moringPlanName = models.CharField(max_length=128,verbose_name="上午计划")
    afternoonPlanName = models.CharField(max_length=128, verbose_name="下午计划")


    def __str__(self):
        return  '%s_%s' %(self.moringPlanName,self.afternoonPlanName)
    class Meta:
        db_table = "Plan"
        verbose_name="计划内容表"
        verbose_name_plural = verbose_name
