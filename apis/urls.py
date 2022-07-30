from django.urls import path
from . import views

urlpatterns = [
    path('Order/', views.getOrder),
    path('Channel/', views.getChannel),
    path('Status/', views.getStatus),
    path('DateTime/', views.getDate_time),
    path('Customer_name/', views.getCustomer_name),
    path('Customer_mobile_number/', views.getCustomer_mobile_number),
    path('Delivery_zone/', views.getDelivery_zone),
    path('ResturantName/', views.getResturantName),


    path('OrderItem/', views.getOrderItem),
    path('OrderAddOnes/', views.getOrderAddOnes),
]
