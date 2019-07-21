# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class QA(models.Model):
    qaName = models.CharField(max_length=100, verbose_name='姓名')
    qapwd = models.CharField(max_length=100,verbose_name="密码")
    qaGroup = models.ForeignKey(to="Group", on_delete=models.CASCADE, verbose_name="所属小组")
    addTime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    # modifyTime = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")

    def __str__(self):
        return  self.qaName
    class Meta:
        db_table = "Users"
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
    typeName = models.CharField(max_length=100, verbose_name="计划名称")
    addTime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.typeName

    class Meta:
        db_table = "PlanType"
        verbose_name = "计划类型表"
        verbose_name_plural = verbose_name

class Plan(models.Model):
    #计划表
    qaName = models.ForeignKey(to="QA",on_delete=models.CASCADE,verbose_name="用户id")
    planTime = models.DateField(auto_now_add=True,verbose_name="计划时间")
    planName = models.ForeignKey(to="PlanType",on_delete=models.CASCADE,verbose_name="计划内容")
    addTime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    modifyTime = models.DateTimeField(auto_now=True,verbose_name="更新时间")


    def __str__(self):
        return  self.planName
    class Meta:
        db_table = "Plan"
        verbose_name="计划表"
        verbose_name_plural = verbose_name
