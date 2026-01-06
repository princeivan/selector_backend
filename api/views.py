from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import (
    User, SoilType, County, Subcounty, Ward,
    Category, Crop, CropVariety, CropSoiltype,
    Aez_zone, LivestockCategory, Livestock,
    PastureCategory, Pasture, PastureVariety
)
from .serializers import *

class CountyViewSet(viewsets.ModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'county_id']

class SubcountyViewSet(viewsets.ModelViewSet):
    queryset = Subcounty.objects.all()
    serializer_class = SubcountySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'subcounty_id', 'county__name']

class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = wardSerializers
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'ward_id', 'subcounty__name']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CropCategorySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializers
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'crop_id', 'category__name']

class CropVarietyViewSet(viewsets.ModelViewSet):
    queryset = CropVariety.objects.all()
    serializer_class = CropVarietySerializers
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['variety', 'crop__name']

class SoilTypeViewSet(viewsets.ModelViewSet):
    queryset = SoilType.objects.all()
    serializer_class = SoilTypeSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'texture', 'fertility']


class CropSoilTypeViewSet(viewsets.ModelViewSet):
    queryset = CropSoiltype.objects.all()
    serializer_class = CropSoilTypeSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['soil_type', 'drainage', 'depth_or_texture']

class AezZoneViewSet(viewsets.ModelViewSet):
    queryset = Aez_zone.objects.all()
    serializer_class = AezSerializers
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['zone_name', 'aez_id']

class LivestockCategoryViewSet(viewsets.ModelViewSet):
    queryset = LivestockCategory.objects.all()
    serializer_class = LivestockCategorySerializers
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class LivestockViewSet(viewsets.ModelViewSet):
    queryset = Livestock.objects.all()
    serializer_class = LivestockSerializers
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['breed', 'livestockcategory__name', 'aez__zone_name']

class PastureCategoryViewSet(viewsets.ModelViewSet):
    queryset = PastureCategory.objects.all()
    serializer_class = PastureCategorySerializers
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class PastureViewSet(viewsets.ModelViewSet):
    queryset = Pasture.objects.all()
    serializer_class = PastureSerializers
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name']

class PastureVarietyViewSet(viewsets.ModelViewSet):
    queryset = PastureVariety.objects.all()
    serializer_class = PastureVaretySerializers
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'pasture_name__name', 'aez__zone_name']