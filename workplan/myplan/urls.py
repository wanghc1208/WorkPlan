from django.urls import path

from myplan.views import add_plan, show_plan

urlpatterns = [
    path('addplan',add_plan),
    path('showplan',show_plan),
]