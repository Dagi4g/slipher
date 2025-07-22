from django.urls import path,include
from . import views

app_name = "slipher_video"
urlpatterns = [
        path("",views.home,name="slipher"),
        path("search/",views.search,name='search'),
        path("watch_video/<str:video_id>/",views.watch_video,name='watch_video'),

        ]

