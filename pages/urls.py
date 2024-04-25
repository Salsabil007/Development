from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomePageView, AboutPageView, FdaProjectView,input_view

urlpatterns = [
    path("",HomePageView.as_view(),name = "home"),
    path("about/",AboutPageView.as_view(),name = "about"),
    path("fda/",FdaProjectView.as_view(),name = "fda"),
    path('input/', input_view, name='input_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
