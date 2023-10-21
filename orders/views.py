import datetime
from django.shortcuts import redirect,render
from carts.models import CartItem
from .forms import OrderForm
from .models import Order
from django.http import HttpResponse

# Create your views here.

def payments(request):
    return render(request,'orders/payments.html')


def place_order(request, total=0, quantity=0,):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    final_fee=0
    tax=0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax=(2*total)/1000
    final_fee=total-tax

    if request.method == 'post':
        form=OrderForm(request.POST)
        if form.is_valid():
            data=Order()
            data.user=current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone_number = form.cleaned_data['phone_number']
            data.email = form.cleaned_data['email']
            data.address_1 = form.cleaned_data['address_1']
            data.address_2 = form.cleaned_data['address_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_total = final_fee
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            form.save()
            yr=int(datetime.date.today().strftime('%y'))
            dt=int(datetime.date.today().strftime('%d'))
            mt=int(datetime.date.today().strftime('%m'))
            d=datetime.date(yr,mt,dt)
            current_date=d.strftime("%yr%m%d")
            order_number=current_date + str(data.id)
            data.order_number=order_number
            data.save()
            form.save()
            order = Order.objects.get(user=current_user,is_ordered=False, order_number=order_number)
            context={
                'order':order,
                'cart_items':cart_items,
                'total':total,
                'tax':tax,
                'final_fee':final_fee
            }
            return render(request,'orders/payments.html',context)
    else:
        return redirect('payments')