from django.urls import path

from . import views

# 최상위 urls에서 url을 파싱하고 받아가지고, 
# path별로 다른 앱으로 분기시켜준다. 
urlpatterns = [
    path('', views.index, name='index'),
]