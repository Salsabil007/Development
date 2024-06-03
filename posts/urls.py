from django.urls import path


from .views import HomePagePost

urlpatterns = [
    path("",HomePagePost.as_view(),name = "homepost"),
] 
