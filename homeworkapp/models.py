from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField()
    phone = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    address = models.TextField(null=False, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f'{self.name}/n{self.email}/n{self.phone}/n{self.address}/n{self.registration_date}'

class Product(models.Model):

    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=False, blank=True, db_index=True)
    price =models.DecimalField(default=0, max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f'{self.name}/n{self.description}/n{self.price}/n{self.quantity}/n{self.created_at}'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="orders")
    sum_order=models.DecimalField(default=0, max_digits=20, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)


