from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class PunditBooking(models.Model):
    EVENT_TYPES = [
        ('housewarming', 'Housewarming'),
        ('wedding', 'Wedding'),
        ('satyanarayan_pooja', 'Satyanarayan Pooja'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES, null=True, blank=True)
    samagri = models.CharField(max_length=10, choices=[("Yes", "Yes"), ("No", "No")], null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.event_type}"
class Banquet(models.Model):
    name = models.CharField(max_length=200)  
    location = models.CharField(max_length=200)  
    starting_price = models.DecimalField(max_digits=10, decimal_places=2) 
    
    description = models.TextField(null=True, blank=True)  
    
    def __str__(self):
        return self.name
class Pundit(models.Model):
    name = models.CharField(max_length=200)  
    education = models.TextField(null=True, blank=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    

    def __str__(self):
        return self.name

class VenueBooking(models.Model):
    EVENT_TYPES = [
        ('wedding', 'Wedding'),
        ('party', 'Party'),
        ('conference', 'Conference'),
        ('other', 'Other'),
    ]
    banquet = models.ForeignKey(Banquet, on_delete=models.CASCADE,null=True, blank=True, related_name='venue_bookings') 
   
   
    
  
    phone = models.CharField(max_length=15, null=True, blank=True)
    
    
    email = models.EmailField(null=True, blank=True)
    
   
    start_date = models.DateField(null=True, blank=True)
    
  
    end_date = models.DateField(null=True, blank=True)
    

    number_of_guests = models.CharField(max_length=50, null=True, blank=True)
    
  
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES, null=True, blank=True)
    
  
    additional_request = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Booking for {self.name} - {self.event_type}"


class PersonalRecommendation(models.Model):
    horoscope = models.CharField(max_length=50, unique=True) 
    education = models.TextField(null=True, blank=True)  
    finance = models.TextField(null=True, blank=True)  
    travel = models.TextField(null=True, blank=True)  
    education_image = models.ImageField(upload_to='images/education/', null=True, blank=True)
    finance_image = models.ImageField(upload_to='images/finance/', null=True, blank=True)
    travel_image = models.ImageField(upload_to='images/travel/', null=True, blank=True)

    def __str__(self):
        return self.horoscope



    
class Order(models.Model):
    VALID_PRODUCTS = [
        ("Panna", "Panna"),
        ("Pushaparaj", "Pushaparaj"),
        ("Rudraksha", "Rudraksha"),
    ]
    product = models.CharField(max_length=255, choices=VALID_PRODUCTS)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    additional_instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order for {self.product} by {self.name}"
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"Enquiry from {self.name} ({self.email})"