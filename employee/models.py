from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when last updated
    
    class Meta:
        abstract = True

class Employee(BaseModel):
    Employee_id =models.CharField(unique=True,max_length=20,blank=False,null=False)
    Employee_name =models.CharField(max_length=100,blank=False,null=False)
    Employee_email = models.EmailField(null=True, blank=True)
    Employee_contact = models.CharField(max_length=10,blank=False,null=False)
    Employee_address = models.TextField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.Employee_name