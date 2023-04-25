from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import User
from .forms import RestaurantRegisterForm,CustomerRegisterForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from .forms import CustomerRegisterForm,RestaurantRegisterForm
from django.views import View
# Create your views here.

def home(request):
        return render(request,'user/home.html')
def about(request):
        return render(request,'user/about.html')
def blog(request):
        return render(request,'user/blog.html')
def contact(request):
        return render(request,'user/contact.html')
def services (request):
        return render(request,'user/services.html')
def testimonial(request):
        return render(request,'user/testimonial.html')
def Feedback(request):
        return render(request,'user/Feedback.html')

    




class CustomerRegisterView(CreateView):
    model = User
    form_class = CustomerRegisterForm
    template_name = 'user/customerregister.html'
    success_url = "/user/login/" 

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_Customer = True
        user.save()
        
        return redirect('user/login.html')    
    


class RestaurantRegisterView(CreateView):
   
    model = User
    form_class = RestaurantRegisterForm
    template_name = 'user/restaurantregister.html'
    success_url = "user/login.html"
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_restaurant = True
        user.save()
        return super().form_valid(form)
   


    


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = "/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_Customer:
                return '/user/home'
            else:
                return("user/customerregister.html")


   
