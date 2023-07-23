from django.db import models

# Create your models here.

class Brand(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'brand'

    
class Category(models.Model):
    name=models.CharField(max_length=255)
    brand=models.ForeignKey(Brand,models.DO_NOTHING)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='category'


class Product(models.Model):
    class IsDisplay(models.IntegerChoices):
        YES= 1,"YES"
        NO=0,"No"

    name=models.CharField(max_length=255)
    brand=models.ForeignKey(Brand,models.DO_NOTHING)
    category=models.ForeignKey(Category,models.DO_NOTHING,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    selling_price=models.IntegerField(blank=True,null=True)
    is_display=models.IntegerField(choices=IsDisplay.choices)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='product'