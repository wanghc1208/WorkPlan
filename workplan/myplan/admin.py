from django.contrib import admin

# Register your models here.
from myplan.models import QA,Group,PlanType,Plan

admin.site.register(QA)
# admin.site.register(Group)
admin.site.register(PlanType)
admin.site.register(Plan)

# class QAAdmin(admin.ModelAdmin):
#     # fields = ('username', 'password')
#     list_display = ("qaName","qapwd","userGroup")

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    # fields = ('username', 'password')
    list_display = ("groupId","groupName","addTime")
