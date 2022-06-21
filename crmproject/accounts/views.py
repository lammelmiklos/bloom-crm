from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
from django.http import HttpResponse

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = { 'orders_queried': orders, 
                'customers_queried': customers,
                'total_customers': total_customers, 
                'total_orders': total_orders,
                'delivered': delivered,
                'pending': pending,
            }

    return render(request, 'accounts/dashboard.html', context=context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products_queried': products })

def customer(request, pk_customer):
    customer = Customer.objects.get(id=pk_customer)
    orders = customer.order_set.all()
    orders_count = orders.count()


    context = {
        'customer': customer,
        'orders': orders,
        'orders_count': orders_count,
    }
    return render(request, 'accounts/customer.html', context)


'''
This is the template structure
-- accounts
---- templates
------ accounts
-------- dashboard.html
-------- profile.html
-------- customer.html

'''