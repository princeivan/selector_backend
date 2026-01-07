from rest_framework import serializers
import re
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import User, County,Subcounty, SoilType, Ward,Warddetails, Category, Crop,Aez_zone,CropSoiltype, CropVariety, LivestockCategory, Livestock,PastureCategory,Pasture, PastureVariety


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
   
    avatar = serializers.ImageField(required=False)
    
    class Meta:
        model = User 
        fields = ["id", "username", "first_name", "last_name", "email","password", "confirm_password", "role","is_active","last_login"]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"required": True},
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True}
        }
    

    def validate_username(self, value):
        # Username should be 3-20 characters, alphanumeric with underscores
        if not re.match(r'^[a-zA-Z0-9_]{3,20}$', value):
            raise serializers.ValidationError(
                "Username must be 3-20 characters and can only contain letters, numbers, and underscores"
            )
        
        # Check if username already exists
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        
        return value


    def validate_email(self, value):
        # Email format validation
        if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', value):
            raise serializers.ValidationError("Please enter a valid email address")
        
        # Check if email already exists
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered")
        
        return value

    def validate_password(self, value):
        # Password validation
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', value):
            raise serializers.ValidationError(
                "Password must be at least 8 characters long and contain uppercase, lowercase, number and special character"
            )
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        return user
        
class AezSerializers(serializers.ModelSerializer):
    class Meta:
        model =Aez_zone
        fields = '__all__'

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'

class SubcountySerializer(serializers.ModelSerializer):
    county = CountySerializer(read_only=True)
    class Meta:
        model = Subcounty
        fields = '__all__'

class SoilTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilType
        fields = '__all__'

class wardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'
        
class wardDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Warddetails
        fields = '__all__'

class CropCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= '__all__'

class CropSerializers(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'
    
class CropSerializers(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class CropSoilTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropSoiltype
        fields = '__all__'


class CropVarietySerializers(serializers.ModelSerializer):
    class Meta:
        model = CropVariety
        fields = '__all__'

class LivestockCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = LivestockCategory
        fields = '__all__'

class LivestockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livestock
        fields = '__all__'

class PastureCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = PastureCategory
        fields = '__all__'

class PastureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pasture
        fields = '__all__'

class PastureVaretySerializers(serializers.ModelSerializer):
    class Meta:
        model = PastureVariety
        fields = '__all__'

