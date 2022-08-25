from django.urls import path,include
from home import views


urlpatterns = [
    path('',views.index,name='homepage'),
    path('login/',views.login,name='log'),
    path('register/',views.register,name='reg'),
    path('logout/',views.logout,name='logout'),
]

