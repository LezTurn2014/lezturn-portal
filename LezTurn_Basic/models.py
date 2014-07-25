from django.db import models
from django.contrib.auth.models import User#, Group, Permission
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=30)
       
class LezUser(User):
    usertype = models.ForeignKey(UserType, related_name='usertype_users') #reverse, means for who belong to a user_type
    store = models.ForeignKey('Store', related_name='store_users')

class Store(models.Model):
    user = models.ForeignKey(LezUser, related_name='user_store', null=False)
    
class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    
    class MPTTMeta:
        order_insertion_by = ['name']

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
class Product(models.Model):
    store = models.ForeignKey(Store, related_name='store_products')
    category = models.ManyToManyField(Category)  
    tag = models.ManyToManyField(Tag)  

class BehaviorStoreType(models.Model):
    name = models.CharField(max_length=50)

class BehaviorProductType(models.Model):
    name = models.CharField(max_length=50)

class BehaviorUserType(models.Model):
    name = models.CharField(max_length=50)
    
class BasicEventLog(models.Model):
    action_time = models.DateField()
    user = models.ForeignKey(LezUser)
    content_type = models.ForeignKey(ContentType)
    user_event_type = models.ForeignKey(BehaviorUserType)
    store_event_type = models.ForeignKey(BehaviorStoreType)
    product_event_type = models.ForeignKey(BehaviorProductType)   
    
class BehaviorEventLog():
    action_time = models.DateField()
    user = models.ForeignKey(LezUser)
    content_type = models.ForeignKey(ContentType)
    user_event_type = models.ForeignKey(BehaviorUserType)
    store_event_type = models.ForeignKey(BehaviorStoreType)
    product_event_type = models.ForeignKey(BehaviorProductType)
    
class UserFollow():
    user = models.ForeignKey(User)
    fan = models.ForeignKey(User)

class StoreFollow():
    store = models.ForeignKey(Store)
    fan = models.ForeignKey(User)

class ProductFollow():
    product = models.ForeignKey(Product)
    fan = models.ForeignKey(User)

class Message():
    sender = models.ForeignKey(User)
    receiver = models.ForeignKey(User)
    action_time = models.DateField()

# class Comment():
#     sender = models.ForeignKey(User)
#     receiver = models.ForeignKey(ContentType)
#     action_time = models.DateField()
    

