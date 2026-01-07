from django.db import models
import uuid
import random
from django.contrib.auth.models import  AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'user')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields['role'] = 'admin'   
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)
    
    
class User(AbstractUser):
    
    ROLE_ADMIN = 'admin'
    ROLE_USER = 'user'

    ROLE_CHOICES = (
        (ROLE_ADMIN, 'Admin'),
        (ROLE_USER, 'Regular User'),
    )
    
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(unique=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    role = models.CharField(max_length=10,
        choices=ROLE_CHOICES,
        default=ROLE_USER)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    @property
    def is_admin(self):
        return self.is_superuser

    def clean(self):
        """
        Prevent invalid role/superuser combinations
        """
        if self.is_superuser and self.role != self.ROLE_ADMIN:
            raise ValidationError("Superuser must have role='admin'")

        if self.role == self.ROLE_ADMIN and not self.is_superuser:
            raise ValidationError("Admin role requires is_superuser=True")

    def save(self, *args, **kwargs):
        self.full_clean()   
        super().save(*args, **kwargs)


class County(models.Model):
    county_id = models.IntegerField(primary_key=True)
    county_name = models.CharField(max_length=100)


    def __str__(self):
        return self.county_name 

class Subcounty(models.Model):
    subcounty_id = models.IntegerField(primary_key=True)
    county= models.ForeignKey(County, on_delete=models.CASCADE, null=True, related_name="subcounties")
    subcounty_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subcounty_name or str(self.pk)
    
class Ward(models.Model):
    ward_id = models.IntegerField(primary_key=True)
    ward_name = models.CharField(max_length=100)
    county= models.ForeignKey(County, on_delete=models.CASCADE, null=True, related_name="ward")
    subcounty = models.ForeignKey(Subcounty,on_delete=models.CASCADE, null=True, related_name="wards")

    def __str__(self):
        return self.ward_name or str(self.pk)


class Warddetails(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True, related_name="wardsdata" )
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    altitude = models.IntegerField(null=True)
    annual_rain = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    annual_temp = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    ke_elev =models.DecimalField(max_digits=10, decimal_places=6, null=True)
    ke_ph =models.DecimalField(max_digits=10, decimal_places=6, null=True)
    lr_rain =models.DecimalField(max_digits=10, decimal_places=6, null=True)
    lr_temp=models.DecimalField(max_digits=10, decimal_places=6, null=True)
    sr_rain=models.DecimalField(max_digits=10, decimal_places=6, null=True)
    sr_temp=models.DecimalField(max_digits=10, decimal_places=6, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ward_name
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name

class Crop(models.Model):
    crop_id = models.IntegerField(primary_key=True)
    crop_name_en = models.CharField(max_length=100, null=True, blank=True)
    crop_en_sw = models.CharField(max_length=100, null=True, blank=True)
    crop_scientificname = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, related_name="crops")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crop_name_en

class SoilType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description =models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class CropVariety(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='varieties')
    variety = models.CharField(max_length=100)

    # Soil chemistry
    minpH = models.DecimalField(max_digits=3, decimal_places=1,null=True, blank=True)
    maxpH = models.DecimalField(max_digits=3, decimal_places=1,null=True, blank=True)

    # Temperature (°C)
    minTemp = models.PositiveIntegerField(null=True, blank=True)
    maxTemp = models.PositiveIntegerField(null=True, blank=True)

    # Rainfall / precipitation (mm)
    minPrep = models.PositiveIntegerField(null=True, blank=True)
    maxPrep = models.PositiveIntegerField(null=True, blank=True)

    # Altitude (meters)
    minAlti = models.PositiveIntegerField(null=True, blank=True)
    maxAlti = models.PositiveIntegerField(null=True, blank=True)

    # Tolerance & preferences
    drought_tolerant = models.BooleanField(default=False)
    pest_tolerant = models.BooleanField(default=False)
    availability = models.BooleanField(default=False)
    farmer_preference = models.BooleanField(default=False)

    def __str__(self):
        return self.variety
class CropSoiltype(models.Model):
    crop_variety = models.ForeignKey(
       CropVariety,
        on_delete=models.CASCADE
    )
    soil_type = models.ForeignKey(
       SoilType,
        on_delete=models.CASCADE 
    )
    
    def __str__(self):
        return f"{self.crop_variety} | {self.soil_type}"
       
class Aez_zone(models.Model):
    aez_id = models.IntegerField(primary_key=True)
    zone_name = models.CharField(max_length=100, blank=True, null=True)
    altitude_range = models.CharField(max_length=100, blank=True, null=True)
    average_annual_rainfall = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
         return f"{self.zone_name} | {self.altitude_range}"

class LivestockCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Livestock(models.Model):
    livestock_id = models.IntegerField(primary_key=True)
    breed = models.CharField(max_length=50, blank=True)
    livestockcategory = models.ForeignKey(LivestockCategory, on_delete=models.CASCADE, related_name="livestocks")
    aez = models.ForeignKey(Aez_zone, on_delete=models.CASCADE, related_name="livestocks")
    
    def __str__(self):
        return self.breed


class PastureCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Pasture(models.Model):
    pasture_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(PastureCategory, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

class PastureVariety(models.Model):
    variety_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    pasture_name = models.ForeignKey(Pasture, on_delete=models.CASCADE)
    aez = models.ForeignKey(Aez_zone, on_delete=models.CASCADE, related_name="pastures")
    def __str__(self):
        return self.name

    



