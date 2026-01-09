from rest_framework import serializers
import re
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['role'] = user.role
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        return token
    

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "role",
            "is_active",
            "last_login",
            "password",
        ]
        extra_kwargs = {
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate_email(self, value):
        qs = User.objects.filter(email=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError("Email already exists")

        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance
        
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

class MarketTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = MarketType
        fields = '__all__'

class DailMarketprioritySerializers(serializers.ModelSerializer):
    class Meta:
        model = DailyMarketPriority
        fields = '__all__'

        
class DashboardStatsSerializer(serializers.Serializer):
    total_counties = serializers.IntegerField()
    total_subcounties = serializers.IntegerField()
    total_wards = serializers.IntegerField()
    total_crops = serializers.IntegerField()
    total_varieties = serializers.IntegerField()
    total_soiltypes = serializers.IntegerField()
    total_aez_zones = serializers.IntegerField()
    total_livestock_categories = serializers.IntegerField()
    total_livestocks = serializers.IntegerField()
    total_pasture_categories = serializers.IntegerField()
    total_pastures = serializers.IntegerField()
    total_pasture_varieties = serializers.IntegerField()