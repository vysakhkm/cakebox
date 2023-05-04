from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator



# Create your models here.
class Cakes(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    price=models.PositiveIntegerField()
    weight=models.CharField(max_length=100)
    shape_choices=[
        ("circle","circle"),
        ("rectangle","rectangle"),
        ("oval","oval"),
    ]
    shape=models.CharField(max_length=300,choices=shape_choices,default="circle")
    layer_choices=[
        ("one","one"),
        ("two","two"),
        ("three","three")
    ]
    layers=models.CharField(max_length=200,choices=layer_choices,default="one")
    image=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.name
    
    @property
    def cake_reviews(self):
        return Reviews.objects.filter(cake=self) 

class Carts(models.Model):
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")
    qty=models.PositiveBigIntegerField(default=1)

class Orders(models.Model):
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("shipped","shipped"),
        ("order-placed","order-placed"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    curDtae=datetime.date.today()
    expDate=curDtae+datetime.timedelta(days=1)
    expected_deliverydate=models.DateField(default=expDate)
    address=models.CharField(max_length=300,null=True)
    matter=models.CharField(max_length=250,null=True)

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    comment=models.CharField(max_length=240)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.comment
    
    