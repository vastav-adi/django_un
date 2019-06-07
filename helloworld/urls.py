from django.urls import path
from helloworld import views

urlpatterns = [
	path('',views.helloworld,name = 'hello_world')
]