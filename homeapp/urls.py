from django.urls import path

from .import views


app_name='homeapp'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('doctor/', views.doctor, name='doctorpage'),
    path('reviews/', views.review, name='reviewpage'),
    path('department/', views.department, name='departmentpage'),
    path('department/<int:pk>', views.department_details, name='departmentdetails'),
    path('test_price_list/', views.test_price_list, name='test_price_list'),
]
