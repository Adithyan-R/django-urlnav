from django.urls import path
from app2 import views
app_name='application2'
urlpatterns=[
    path('app2/',views.app2_home,name='app2'),
]