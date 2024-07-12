from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Project(models.Model):
    colony_name = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    
    
    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project/')

    def __str__(self):
        return f"Image for {self.project.name}"


class Property(models.Model):
    name = models.CharField(max_length=255)
    price_range = models.CharField(max_length=255)
    builder_name = models.CharField(max_length=255)
    property_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='properties/')
    project_size = models.CharField(max_length=100, blank=True)
    possession_date = models.DateField(null=True, blank=True)
    total_units = models.IntegerField(null=True, blank=True)
    total_towers = models.IntegerField(null=True, blank=True)
    project_type = models.CharField(max_length=255, blank=True)
    plot_size = models.CharField(max_length=255, blank=True)
    project_status = models.CharField(max_length=255, blank=True)
    rera_registraion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.property.name} Image"


class HomeLoanOffer(models.Model):
    property = models.ForeignKey(Property, related_name='loan_offers', on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=255)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    bank_img = models.ImageField(upload_to='bank_img/', blank=True)


class CustomerReview(models.Model):
    property = models.ForeignKey(Property, related_name='customer_reviews', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    review_date = models.DateField(default=timezone.now)# Create your models here.
    
class Amenity(models.Model):
    property = models.ForeignKey(Property, related_name='amenities', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='amenity_icons/', blank=True)  # Assuming you will upload icons via admin


class Press(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class PressImage(models.Model):
    press = models.ForeignKey(Press, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='press_images/')

    def __str__(self):
       return f"Image for {self.press.title}"

class Listing(models.Model):
    LISTING_TYPES = [
        ('plot', 'Plot'),
        ('commercial', 'Commercial Space'),
        ('flat', 'Flat/Villa'),
    ]
    
    listing_type = models.CharField(max_length=20, choices=LISTING_TYPES)
    project_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    plot_type = models.CharField(max_length=255, null=True, blank=True)
    listing_address = models.CharField(max_length=255)
    width = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    length = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    total_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    facing = models.CharField(max_length=50, null=True, blank=True)
    open_side = models.CharField(max_length=50, null=True, blank=True)
    transaction_type = models.CharField(max_length=50)
    possession_status = models.CharField(max_length=50)
    expected_price = models.DecimalField(max_digits=20, decimal_places=2)
    price_per_sqft = models.DecimalField(max_digits=20, decimal_places=2)
    amenities = models.JSONField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    super_buildup_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    floor_number = models.CharField(max_length=50, null=True, blank=True)
    furnished_status = models.CharField(max_length=50, null=True, blank=True)
    flat_size = models.CharField(max_length=50, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('listing_detail', kwargs={'pk': self.pk})