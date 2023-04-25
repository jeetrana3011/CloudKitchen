from django.contrib import admin
from .models import User,Address,Customer,Restaurant

# Register your models here.
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Restaurant)
