from django.db import models
from acounts.models import Account
from store.models import Product,Variation
# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    payment_id=models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid=models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.payment_id



class Order(models.Model):
    STATUS =(
        ('New','New'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled')
    )

    user = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)
    payment_id=models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    order_number=models.CharField(max_length=100)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=100)
    address_1=models.CharField(max_length=100)
    address_2=models.CharField(max_length=100, blank=True)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    order_total=models.FloatField()
    tax=models.FloatField()
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip=models.CharField(blank=True,max_length=100)
    is_ordered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_address(self):
        return f'{self.address_1} {self.address_2}'


    def __str__(self):
        return self.first_name


class OrderProduct(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation=models.ForeignKey(Variation,on_delete=models.CASCADE)
    color= models.CharField(max_length=100)
    size= models.CharField(max_length=100)
    quantity = models.IntegerField()
    product_price=models.FloatField()
    ordered=models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name


