#Accounts/Views.py
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from .views import *

urlpatterns = [
      path('', views.index, name="index"),
      #path('register/', views.user_register, name="User_register"),
      path('login/', views.login, name="login"),
      path('logout/', views.logout, name="logout"),
      path('join/', views.join, name="join"),
      path('updateuser/', views.update_user, name="Update_User"),
      path('profile_updated/', views.profile_updated, name = 'profile_updated'),
      path('userhome/', views.userhome, name = 'User Home'),
      #path('update/', views.update_profile, name="Update_Profile"),
      path('profile/<int:pid>',views.profile, name="Profile"),
      path('users/', views.reg_users, name='Reg_users'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
