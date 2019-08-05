from django.contrib import admin

# Register your models here.
from myplan.models import User, Group, PlanType, Plan


admin.site.register(PlanType)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name","password","group","addTime")

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("groupName","addTime")

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("uname","planTime","PlanName")
