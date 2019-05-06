from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    ''' profile for every user '''
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="profile_user")
    role_choice=(('retailer',"retailer"),('distributor',"distributor"),('supplier',"supplier"))
    role=models.CharField(max_length=15,choices=role_choice,default=None)
    is_supplier=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Supplier(models.Model):
    profile=models.OneToOneField('UserProfile',on_delete=models.CASCADE,limit_choices_to={'role':'supplier'},related_name='supplier')

    def __str__(self):
        return self.profile.user.username

class Distributor(models.Model):
    profile=models.OneToOneField('UserProfile',on_delete=models.CASCADE,limit_choices_to={'role':'distributor'},related_name='distributor')
    def __str__(self):

        return self.profile.user.username

class Retailer(models.Model):
    profile=models.OneToOneField('UserProfile',on_delete=models.CASCADE,limit_choices_to={'role':'retailer'},related_name='retailer')

    def __str__(self):
        return self.profile.user.username

class stock(models.Model):
    user=models.ForeignKey('UserProfile',on_delete=models.CASCADE,limit_choices_to={'is_supplier':False},related_name='stock')
    quantity=models.IntegerField(default=0)
    demand=models.IntegerField(default=1)
    medicine=models.ForeignKey('medicine',on_delete=models.CASCADE,related_name='medicine_stock')
    lead_time=models.IntegerField(null=True,blank=True)

class medicine(models.Model):
    name=models.CharField(max_length=50,null=False)
    price=models.IntegerField()
    description=models.TextField(max_length=250,null=True,blank=True)
    user=models.ManyToManyField('UserProfile',through='stock')

    def __str__(self):
        return self.name

class Order(models.Model):
    medicine=models.ForeignKey('medicine',on_delete=models.CASCADE,related_name='medicine_orders')
    quantity=models.IntegerField(default=0)
    placed_by=models.ForeignKey('UserProfile',on_delete=models.CASCADE,limit_choices_to={'is_supplier':False},related_name='order_placed')
    placed_to=models.ForeignKey('UserProfile',on_delete=models.CASCADE,related_name='order_recieved')
    status_choice=(('Pending',"Pending"),('Approved',"Approved"),('Declined',"Declined"))
    status=models.CharField(max_length=15,choices=status_choice,default=None)
    date_time=models.DateTimeField('date_placed')
    order_id=models.CharField(max_length=5,null=True,blank=True)
