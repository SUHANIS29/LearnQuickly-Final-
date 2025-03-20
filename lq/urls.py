"""
URL configuration for lq project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


from django.urls import path
from lq import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='sign'),
    path('login/',views.loginp,name='logn'),
    path('home/',views.homepage,name='home'),
    path('logout/',views.lgout,name='logout'),
    path('forgot_password/',views.forgotp,name='forgotpaswd'),
    path('reset_password/<str:user>/',views.resetpas,name='resetpaswd'),
    path('',views.lq,name='lq'),
    path('about/',views.about,name='about'),
    path('newexp/',views.newexp,name='newexp'),
    path('lq2/',views.lq2,name='lq2'),
    path('streamlit_summary/',views.summary,name='s_summ'),
    path('s_flowchart/',views.flow,name='flow'),
    path('s_mcq/',views.mcq,name='mcq'),
    path('s_flash/',views.flash,name='flash'),
    
    path('inference/',views.sum,name='sum'),
    path('quizapp/',views.quiz,name='quiz'),
    path('try/',views.flashc,name='flashc'),
    path('chart/',views.chartt,name='chartt')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)