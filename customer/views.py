from django.shortcuts import render,redirect
from django.views import View
from .models import MenuItem, Category, OrderModel
from django.core.mail import send_mail
from user.models import Address


class Order(View):
    def get(self, request, *args, **kwargs):        
        # get every item from each category
        maincourses = MenuItem.objects.filter(
            category__name__contains='Maincourse')
        starters= MenuItem.objects.filter(category__name__contains='Starters')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')

        # pass into context
        context = {
            'maincourses':maincourses,
            'starters': starters,
            'desserts': desserts,
            'drinks': drinks,
        }

        # render the template
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order=OrderModel.objects.create(
                price=price,
                name=name,
                email=email,
                address=address,
                city=city,
                pincode=pincode,
            )
        order.items.add(*item_ids)


        body=('Thank you for your order! Your Order is being made and will be deliver soon \n'
                f'your total:{price}\n'
                'Thank You again for your order!')


        send_mail( 
                'Thank you for Your Order!',
                body,
                'jeetr1813@gmail.com',
                [email],
                fail_silently=False
            )
        
            

        context={
            'items': order_items['items'],
            'price': price
            }

        return redirect('orderconfirm', pk=order.pk)
        
    
class OrderConformation(View):
    def get(self,request,pk,*args, **kwargs):    
        order= OrderModel.objects.get(pk=pk)

        context ={
            'pk':order.pk,
            'items':order.items,
            'price':order.price,
        }

        return render(request, 'customer/orderconfirm.html', context)
        
    def post(self,request,pk,*args, **kwargs):
            print(request.body)

class OrderPayConformation(View):
    def get(self,request,pk,*args, **kwargs):
        return render(request,'customer/orderpayconfirm.html')