from email.policy import default
from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date

# Create your models here
    
class Product(models.Model):
    TYPE = (
        ('Inflow', 'Inflow'),
        ('Outflow', 'Outflow'),
    )
    
    UNIT = (
        ('Ton', 'Ton'),
        ('Kg', 'Kg'),
        ('Lt', 'Lt'),   
    ) 

    image = models.ImageField('Image', null=True)
    name = models.CharField('Company Name', max_length=255, null=True)
    description = models.CharField('Description', max_length=500, null=True)
    type = models.CharField('Type', choices=TYPE, max_length=100, null=True)
    value = models.FloatField('Expected Value')
    unit = models.CharField("Unit", choices=UNIT, max_length=100, null=True)

    def __str__(self):
        return (str(self.id) + " | " + self.name)

class Company(models.Model):
    CLASSIFICATION = (
        ('Micro', 'Micro'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    logo = models.ImageField('Logo', null=True)
    name = models.CharField('Company Name', max_length=255, null=True)
    cin = models.CharField('Company Identification Number', max_length=21, null=True)
    address = models.CharField('Address', max_length=500, null=True)
    classification = models.CharField('Classification', choices=CLASSIFICATION, max_length=100, null=True)
    industry = models.CharField('Industry Type', max_length=100, null=True)
    revenue = models.FloatField('Revenue per Annum')
    
    inflow = models.ManyToManyField(Product, related_name="Inflow_Products", blank=True)
    outflow = models.ManyToManyField(Product, related_name="Outflow_Products", blank=True)

    def __str__(self):
        return (str(self.id) + " | " + self.name)

class Quotation(models.Model):
    UNIT = (
        ('Ton', 'Ton'),
        ('Kg', 'Kg'),
        ('Lt', 'Lt'),
    )
    
    STATUS = (
        ('Requested', 'Requested'),
        ('Acknowledged', 'Acknowledged'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    )

    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    seller = models.OneToOneField(Company, related_name="Seller", null=True, on_delete=models.CASCADE)
    buyer = models.OneToOneField(Company, related_name="Buyer", null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField("Date Created", auto_now_add=True)
    date_accepted = models.DateTimeField("Date Accepted")

    target = models.FloatField("Target Price")
    quantity = models.IntegerField("Quantity")
    unit = models.CharField("Unit", max_length=100, choices=UNIT, null=True)

    status = models.CharField('Status', choices=STATUS, max_length=100, null=True)

    def __str__(self):
        return (str(self.id) + " | " + str(self.product.name) + " | " + str(self.seller.name) + " | " + str(self.buyer.name) + " | " + str(self.date_created.date))

class Transaction(models.Model):
    UNIT = (
        ('Ton', 'Ton'),
        ('Kg', 'Kg'),
        ('Lt', 'Lt'),
    ) 

    STATUS = (
        ('Initiated', 'Initiated'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    )

    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    paid = models.FloatField("Paid Amount")
    unpaid = models.FloatField("Unpaid Amount")
    total = models.FloatField("Total Amount")
    commission = models.FloatField("Commission")
    
    quantity = models.IntegerField("Quantity")
    unit = models.CharField("Unit", max_length=100, choices=UNIT, null=True)

    status = models.CharField('Status', choices=STATUS, max_length=100, null=True)
    quotation = models.OneToOneField(Quotation, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.id) + " | " + str(self.product.name) + " | " + str(self.seller.name) + " | " + str(self.buyer.name) + " | " + str(self.date_created.date))
    
class Inventory(models.Model):
    TYPE = (
        ('Inflow', 'Inflow'),
        ('Outflow', 'Outflow'),
    ) 

    UNIT = (
        ('Ton', 'Ton'),
        ('Kg', 'Kg'),
        ('Lt', 'Lt'),
    ) 

    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    type = models.CharField("Type", max_length=100, choices=TYPE, null=True)
    quantity = models.IntegerField("Quantity", null=True) 
    required = models.IntegerField("Required Quantity", null=True)
    unit = models.CharField("Unit", max_length=100, choices=UNIT, null=True)
    value = models.FloatField("Value", null=True)
    transactions = models.ManyToManyField(Transaction, blank=True)
    last_updated = models.DateTimeField("Date Last Updated", null=True)  

    def __str__(self):
        return (str(self.id) + " | " + str(self.product.name) + " | " + str(self.seller.name) + " | " + str(self.buyer.name) + " | " + str(self.date_created.date))
    
class DeliveryTracker(models.Model):
    UNIT = (
        ('Ton', 'Ton'),
        ('Kg', 'Kg'),
        ('Lt', 'Lt'),
    ) 

    STATUS = (
        ('Ordered', 'Ordered'),
        ('Shipped', 'Shipped'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
    )

    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)

    fromAddress = models.CharField('From Address', max_length=500, null=True)
    toAddress = models.CharField('To Address', max_length=500, null=True)

    orderDate = models.DateTimeField("Order Date", auto_now_add=True, null=True)
    shipDate = models.DateTimeField("Shipped Date", null=True)
    estimatedDate = models.DateTimeField("Estimated Delivery Date", null=True)
    deliveryDate = models.DateTimeField("Delivery Date", null=True)
    
    quantity = models.IntegerField("Quantity")
    unit = models.CharField("Unit", max_length=100, choices=UNIT, null=True)

    status = models.CharField('Status', choices=STATUS, max_length=100, null=True)
    
    transaction = models.OneToOneField(Transaction, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.id) + " | " + str(self.product.name) + " | " + str(self.seller.name) + " | " + str(self.buyer.name) + " | " + str(self.orderDate.date))

