from django.db import models


class Blogpost(models.Model):
    id = models.AutoField
    Date = models.DateField()
    Title = models.CharField(max_length=150)
    Description = models.TextField()
    Image = models.ImageField(upload_to='pics')


class Books(models.Model):
    id = models.AutoField
    Date = models.DateField()
    Title = models.CharField(max_length=150)
    Description = models.TextField()
    Image = models.ImageField(upload_to='bookspic')
    Category = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Pages = models.IntegerField(default=0)
    Price = models.IntegerField(default=0)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()


class DeliveryDetails(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    pincode = models.CharField(max_length=6)
    house_no = models.CharField(max_length=15)
    area = models.CharField(max_length=30)
    landmark = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=40)


