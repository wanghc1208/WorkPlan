from django.contrib import admin

# Register your models here.
from myplan.models import QA,Group,PlanType,Plan

# admin.site.register(QA)
# admin.site.register(Group)
admin.site.register(PlanType)
admin.site.register(Plan)

@admin.register(QA)
class QAAdmin(admin.ModelAdmin):
    # fields = ('username', 'password')
    list_display = ("qaName","qapwd","qaGroup","addTime")

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    # fields = ('username', 'password')
    list_display = ("groupName","addTime")
