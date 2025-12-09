from django.db import models

# Create your models here.

class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'Starter'),
        ('main', 'Main'),
        ('dessert', 'Dessert'),
        ('drink', 'Drink'),
    ]
    dish_name = models.CharField(max_length=100, verbose_name="dish's name")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="category")
    image = models.ImageField(upload_to='media/', verbose_name="Image")
    
    def str(self):
        return self.dish_name

class ContactMessage(models.Model):
    sender_name = models.CharField(max_length=100, verbose_name="Sender's name")
    sender_email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    sent_at = models.DateTimeField(auto_now=True, verbose_name="Sent at")
    
    def __str__(self):
        return f"Message from {self.sender_name}  ({self.sender_email})"

class Order(models.Model):
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    name = models.CharField(max_length=100, verbose_name="Customer's name")
    phone = models.CharField(max_length=20, verbose_name="Phone number")
    address = models.TextField(verbose_name="Delivery address")
    
    def __str__(self):
        return f"Order of {self.quantity} by {self.name}"
