from django.db import models

class AccountActivity(models.Model):
#     email = models.EmailField(unique=True)
    account = models.CharField(max_length = 25)
    activity = models.CharField(max_length = 25)
    type = models.CharField(max_length = 25)
    typename = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    ipaddress = models.CharField(max_length = 15)
    
    class Meta:
        db_table = "account_activity"
    
    
    
    
    
class ContainerActivity(models.Model):
#     email = models.EmailField(unique=True)
    account = models.CharField(max_length = 25)
    activity = models.CharField(max_length = 25)
    type = models.CharField(max_length = 25)
    typename = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    ipaddress = models.CharField(max_length = 15)
    class Meta:
        db_table = "container_activity"
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        print 'save'
        if True:
            return
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        
        
if __name__ == '__main__':
    ContainerActivity.objects.create()
        
        
        
        