from django.db import models

# Create your models here.
class Users(models.Model):
    #y用户表
    userName = models.CharField(max_length=100,verbose_name="姓名")
    # userGroup = models.CharField(max_length=100,verbose_name="所属小组")
    userGroup = models.ForeignKey(to="Group", on_delete=models.CASCADE, verbose_name="所属小组")
    planTime = models.DateField(auto_now_add=False,verbose_name="计划时间")
    userPlan = models.ForeignKey(to="Plan",on_delete=models.CASCADE,verbose_name="计划名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")


    def __str__(self):
        return  self.userName
    class Meta:
        db_table = "用户表"
        verbose_name="用户表"
        verbose_name_plural = verbose_name

class Group(models.Model):
    #小组表
    groupID = models.AutoField(primary_key=True,verbose_name="小组ID")
    groupName = models.CharField(max_length=100,verbose_name="小组名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")


    def __str__(self):
        return  self.groupName
    class Meta:
        db_table = "小组表"
        verbose_name="小组表"
        verbose_name_plural = verbose_name

class Plan(models.Model):
    #计划表
    planID = models.AutoField(primary_key=True,verbose_name="计划ID")
    planName = models.CharField(max_length=100,verbose_name="计划名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")


    def __str__(self):
        return  self.planName
    class Meta:
        db_table = "计划表"
        verbose_name="计划表"
        verbose_name_plural = verbose_name


class PlanType(models.Model):
    # 计划类型表
    typeName = models.CharField(primary_key=True,max_length=100, verbose_name="计划名称")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.typeName

    class Meta:
        db_table = "计划类型表"
        verbose_name = "计划类型表"
        verbose_name_plural = verbose_name