from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('sections/<int:id>',views.sections,name="sections"),
]