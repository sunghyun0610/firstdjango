
from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index),
    path('create/',views.create),
    path('read/<id>/',views.read)

]

# 아무것도 입력하지 않고 들어왔을때 views.index함수가 실행

