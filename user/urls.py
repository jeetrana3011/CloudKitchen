from django.contrib import admin
from django.urls import path,include
from .views import RestaurantRegisterView,CustomerRegisterView,UserLoginView,home,about
from django.contrib.auth.views import LogoutView
from django.views import View
from .import views
urlpatterns = [
 
 path('restaurantregister/',RestaurantRegisterView.as_view(),name='restaurantregister'),
 path('customerregister/',CustomerRegisterView.as_view(),name='customerregister'),
 path('login/',UserLoginView.as_view(),name='login'),
 path('logout/',LogoutView.as_view(),name='logout'),
 path('home/',views.home,name='home'),
 path('blog/',views.blog,name='blog'),
 path('about/',views.about,name='about'),
 path('contact/',views.contact,name='contact'),
 path('services/',views.services,name='services'),
 path('testimonial/',views.testimonial,name='testimonial'),
 path('contact/user/Feedback/',views.Feedback,name='Feedback'),
 

]