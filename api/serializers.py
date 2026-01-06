from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import User, County,Subcounty, SoilType, Ward, Category, Crop,Aez_zone,SoilCondition, CropVariety, LivestockCategory, Livestock,PastureCategory,Pasture, PastureVariety

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

class SoilConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilCondition
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

