from django.urls import path

from .views import HomePageView, AboutPageView, FdaProjectView

urlpatterns = [
    path("",HomePageView.as_view(),name = "home"),
    path("about/",AboutPageView.as_view(),name = "about"),
    path("fda/",FdaProjectView.as_view(),name = "fda"),
]