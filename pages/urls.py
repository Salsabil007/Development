from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomePageView, AboutPageView, FdaProjectView

urlpatterns = [
    path("",HomePageView.as_view(),name = "home"),
    path("about/",AboutPageView.as_view(),name = "about"),
    path("fda/",FdaProjectView.as_view(),name = "fda"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
