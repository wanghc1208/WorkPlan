from django.contrib import admin

# Register your models here.
from myplan.models import QA,Group,PlanType,Plan

admin.site.register(QA)
# admin.site.register(Group)
admin.site.register(PlanType)
admin.site.register(Plan)
class UsersAdmin(admin.ModelAdmin):
    # fields = ('username', 'password')
    list_display = ("userName","password","userGroup")
admin.site.register(Group)
class GroupAdmin(admin.ModelAdmin):
    # fields = ('username', 'password')
    list_display = ("groupId","groupName","addTime")
