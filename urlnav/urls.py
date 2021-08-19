"""urlnav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from app1 import urls
from app2 import urls
import app2.views
import app1.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('application1/',include('app1.urls')),
    path('application2/',include('app2.urls')),
    path('app1/',app1.views.app1_msg,name='app1'),
    path('app2/',app2.views.app2_msg,name='app2'),
]
