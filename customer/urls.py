from django.contrib import admin
from django.urls import path,include
from .views import Order,OrderConformation,OrderPayConformation
from django.views import View

urlpatterns = [

path('order/', Order.as_view(),name='order'),
path('orderconfirm/<int:pk>', OrderConformation.as_view(),name='orderconfirm'),
path('orderpayconfirm/<int:pk>', OrderPayConformation.as_view(),name='orderpayconfirm'),

]