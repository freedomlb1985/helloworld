from django.db import models
from account.models import Account

class AccountActivity(models.Model):
#     email = models.EmailField(unique=True)
    account = models.ForeignKey(Account, unique=False)
    activity = models.CharField(max_length = 25)
    type = models.CharField(max_length = 25)
    typename = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    ipaddress = models.CharField(max_length = 15)
    
    class Meta:
        db_table = "account_activity"
    
    
    
    
    
class ContainerActivity(models.Model):
#     email = models.EmailField(unique=True)
    account = models.ForeignKey(Account, unique=False)
    activity = models.CharField(max_length = 25)
    type = models.CharField(max_length = 25)
    typename = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    ipaddress = models.CharField(max_length = 15)
    class Meta:
        db_table = "container_activity"
        
        
        
        
        
        
        