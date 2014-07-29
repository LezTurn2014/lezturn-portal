from django.db import models
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User#, Group, Permission


class LezUser(User):
    store = models.ForeignKey('Store', related_name='store_users')
    
# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50, unique=True)
    open_date = models.DateField()
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
    description = models.CharField(max_length=500)
    amount = models.IntegerField()
    price = models.FloatField()

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
    user = models.ForeignKey(LezUser)
    fan = models.ForeignKey(LezUser)

class StoreFollow():
    store = models.ForeignKey(Store)
    fan = models.ForeignKey(LezUser)

class ProductFollow():
    product = models.ForeignKey(Product)
    fan = models.ForeignKey(LezUser)

class Message():
    sender = models.ForeignKey(LezUser)
    receiver = models.ForeignKey(LezUser)
    action_time = models.DateField()

# class Comment():
#     sender = models.ForeignKey(User)
#     receiver = models.ForeignKey(ContentType)
#     action_time = models.DateField()
    

