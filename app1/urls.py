from django.urls import path
from app1 import views
app_name='application1'
urlpatterns=[
    path('app1/',views.app1_home,name='app1'),
]