from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product' , on_delete=models.SET_NULL , null=True , related_name='+')

class Product(models.Model):
    title = models.CharField(max_length=255) 
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey(Collection ,on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD   = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE , 'BRONZE'),
        (MEMBERSHIP_SILVER , 'SILVER'),
        (MEMBERSHIP_GOLD   , 'GOLD' )
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length= 255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1 , choices=MEMBERSHIP_CHOICES , default= MEMBERSHIP_BRONZE )
    class Meta :
        indexes = [
            models.Index(fields= ['last_name' , 'first_name'])
        ]
    
class Order(models.Model):
    payment_pending = 'P'
    payment_complete = 'C'
    payment_failed = 'F'
    
    payment_status = [
        (payment_pending , 'Pending'),
        (payment_complete , 'Complete'),
        (payment_failed , 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1 , choices=payment_status ,default= payment_pending )
    customer = models.ForeignKey(Customer , on_delete= models.PROTECT)
    
class OrderItem(models.Model):
        order = models.ForeignKey(Order, on_delete=models.PROTECT)
        product = models.ForeignKey(Product , on_delete=models.PROTECT)
        quantity = models.PositiveBigIntegerField()
        unit_price = models.DecimalField(max_digits=6 ,decimal_places=2)
        
    
    
class Address(models.Model):
        street = models.CharField(max_length=255 , help_text="this is the street name")
        city = models.CharField(max_length=255)
        customer = models.OneToOneField(Customer, on_delete=models.CASCADE , primary_key=True)
        street_number = models.IntegerField(default=5 , help_text='street num , it accepts negative values as US country accepts negative values')
        zip_code = models.PositiveIntegerField(default= 11000)

        
class Cart(models.Model):
        created_at = models.DateTimeField(auto_now_add=True) 
    
    
class CartItem(models.Model):
        cart = models.ForeignKey(Cart ,  on_delete=models.CASCADE)
        product = models.ForeignKey(Product , on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField()      
    
            
    
        
        
    
        