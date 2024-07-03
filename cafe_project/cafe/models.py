from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.username

class Admin(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Storage(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

class Vertical(models.Model):
    CATEGORY_CHOICES = [
        ('Cake', 'کیک'),
        ('Hot Drink', 'نوشیدنی گرم'),
        ('Cold Drink', 'نوشیدنی سرد'),
        ('Breakfast', 'صبحانه'),
    ]
    name = models.CharField(max_length=255, unique=True, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    sugar = models.IntegerField()
    coffee = models.IntegerField()
    flour = models.IntegerField()
    chocolate = models.IntegerField()
    vertical = models.ForeignKey(Vertical, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', db_column='username')
    products = models.CharField(max_length=255)
    purchase_amount = models.IntegerField()
    order_type = models.BooleanField()

    def __str__(self):
        return f'Order {self.order_id} by {self.username}'

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='order_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} in Order {self.order.order_id}'
