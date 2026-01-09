from django.db import models
import uuid
import random
from django.contrib.auth.models import  AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)

        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("role", User.ROLE_USER)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", User.ROLE_ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)
    
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_ADMIN = "admin"
    ROLE_ICT = "ict"
    ROLE_RESEARCHER = "researcher"
    ROLE_USER = "user"

    ROLE_CHOICES = (
        (ROLE_ADMIN, "Admin"),
        (ROLE_ICT, "ICT Officer"),
        (ROLE_RESEARCHER, "Researcher"),
        (ROLE_USER, "Regular User"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ROLE_USER)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class County(models.Model):
    county_id = models.IntegerField(primary_key=True)
    county_name = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return self.county_name 

class Subcounty(models.Model):
    subcounty_id = models.IntegerField(primary_key=True)
    county= models.ForeignKey(County, on_delete=models.CASCADE, null=True, related_name="subcounties")
    subcounty_name = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.subcounty_name or str(self.pk)
    
class Ward(models.Model):
    ward_id = models.IntegerField(primary_key=True)
    ward_name = models.CharField(max_length=100, db_index=True)
    county= models.ForeignKey(County, on_delete=models.CASCADE, null=True, related_name="ward")
    subcounty = models.ForeignKey(Subcounty,on_delete=models.CASCADE, null=True, related_name="wards")
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.ward_name or str(self.pk)


class Warddetails(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True, related_name="wardsdata" , db_index=True)
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
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.ward_name
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.category_name

class Crop(models.Model):
    crop_id = models.IntegerField(primary_key=True)
    crop_name_en = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    crop_en_sw = models.CharField(max_length=100, null=True, blank=True)
    crop_scientificname = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, related_name="crops")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crop_name_en

class SoilType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description =models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

class CropVariety(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='varieties')
    variety = models.CharField(max_length=100)
    release_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="Year the variety was released"
    )

    owner = models.CharField(
        max_length=250,
        blank=True,
        help_text="Institution or breeder owning the variety"
    )

    maintainer_seed_source = models.CharField(
        max_length=250,
        blank=True,
        help_text="Seed source or maintaining institution"
    )

    maturity_duration_min_months = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    maturity_duration_max_months = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    yield_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    yield_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    yield_unit = models.CharField(
        max_length=50,
        default="t/ha",
        help_text="Yield unit e.g. t/ha, kg/acre"
    )
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
    special_remarks = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    

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
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
         return f"{self.zone_name} | {self.altitude_range}"

class LivestockCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Livestock(models.Model):
    livestock_id = models.IntegerField(primary_key=True)
    breed = models.CharField(max_length=50, blank=True)
    livestockcategory = models.ForeignKey(LivestockCategory, on_delete=models.CASCADE, related_name="livestocks")
    aez = models.ForeignKey(Aez_zone, on_delete=models.CASCADE, related_name="livestocks")
    prod_system= models.CharField(max_length=200, blank=True, null=True)
    disease_resistance = models.CharField(max_length=200, blank=True, null=True)	
    feed_requirements = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.breed


class PastureCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Pasture(models.Model):
    pasture_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(PastureCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

class PastureVariety(models.Model):
    variety_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    pasture_name = models.ForeignKey(Pasture, on_delete=models.CASCADE)
    aez = models.ForeignKey(Aez_zone, on_delete=models.CASCADE, related_name="pastures")
    water_requirements = models.CharField(max_length=50, blank=True)	
    persistence = models.CharField(max_length=50, blank=True)
    biomass_production = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name
class MarketType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        verbose_name = "Market Type"
        verbose_name_plural = "Market Types"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class DailyMarketPriority(models.Model):
    market_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField()	
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    altitude_mode = models.PositiveSmallIntegerField(default=0)
    tessellate = models.BooleanField(default=False)
    extrude = models.BooleanField(default=False)
    visibility = models.BooleanField(default=True)
    draw_order = models.PositiveSmallIntegerField(default=0)
    county = models.ForeignKey(
        County,
        on_delete=models.CASCADE,
        related_name="markets",
        db_index=True,
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Latitude coordinate"
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Longitude coordinate"
    )
    icon = models.ImageField(
        upload_to="market_icons/",
        blank=True,
        null=True
    )
    market_type = models.ForeignKey(
        MarketType,
        on_delete=models.PROTECT,
        related_name="markets"
    )
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["county"]),
            models.Index(fields=["market_type"]),
            models.Index(fields=["start_time", "end_time"]),
        ]
        verbose_name = "Daily Market Priority"
        verbose_name_plural = "Daily Market Priorities"

    def __str__(self):
        return f"{self.market_name} ({self.county})"
    
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time")


    



