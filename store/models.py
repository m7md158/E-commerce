from django.db import models
import datetime

# Category of Products
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name


# Customer
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} '
    

# All of our Products
class Product(models.Model):
    name = models.CharField(max_length=255, blank=True,null=True)
    price = models.DecimalField(default=0 , decimal_places=2 , max_digits=6 )
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1)
    image = models.ImageField(upload_to='uploads/product', blank=True, null=True)
    # Add sale stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0 , decimal_places=2 , max_digits=6)
    
    def __str__(self):
        return self.name

# Order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20 , default='', blank=True)
    date = models.DateField(default=datetime.datetime.now)
    status =models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.product
    