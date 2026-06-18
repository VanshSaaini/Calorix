"""
URL configuration for calorix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from home.views import home, signup, login, logout_view,aboutUs
from BMI import views as bmi_views
from BMR import views as bmr_views
from dashboard.views import dashboard, chart_data

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('logout/',logout_view, name='logout'),
    path('', home, name="home"),
    path('aboutUs/',aboutUs,name="aboutUs"),
    path('dashboard/', dashboard, name="dashboard"),

    path('accounts/', include('allauth.urls')),

    path('api/data/', chart_data, name='api-data'),

    path('BMR/', bmr_views.bmr, name="bmr"),
    path('BMI/', bmi_views.bmi, name="bmi"),

    path('admin/', admin.site.urls),
]
