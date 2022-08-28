from django.urls import path,include
from product import views


urlpatterns = [
    path('',views.proindex,name='procoll'),
    path('prodetails/',views.prodeta,name='prodeta'),
    path('billing/',views.billed,name='bil'),
]
