from django.urls import paths

from profiles_api import views


urlpatters = [
path('hello-view/', views.HelloApiView.as_view()),
]
