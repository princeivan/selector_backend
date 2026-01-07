from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from .permissions import IsAdminICTOrResearcherReadUpdate, IsAdmin
from rest_framework.throttling import UserRateThrottle
from django.core.validators import validate_email
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import (
    User, SoilType, County, Subcounty, Ward,
    Category, Crop, CropVariety, CropSoiltype,
    Aez_zone, LivestockCategory, Livestock,
    PastureCategory, Pasture, PastureVariety
)
from .serializers import *

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CustomRateThrottle(UserRateThrottle):
    rate = '5/minute'  # 5 requests per minute

class UserViewSet(viewsets.ModelViewSet):
    """
    Admin-only User Management
    """
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("-created_at")
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        user = self.request.user

        if user.role == User.ROLE_ADMIN:
            return self.queryset

        raise PermissionDenied("You do not have permission to view users.")

    def perform_create(self, serializer):
        if self.request.user.role != User.ROLE_ADMIN:
            raise PermissionDenied("Only admins can create users.")
        serializer.save()

    def perform_update(self, serializer):
        if self.request.user.role != User.ROLE_ADMIN:
            raise PermissionDenied("Only admins can update users.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.role != User.ROLE_ADMIN:
            raise PermissionDenied("Only admins can delete users.")

        # Soft delete (recommended)
        instance.is_active = False
        instance.save()

    def perform_destroy(self, instance):
        if instance == self.request.user:
            raise PermissionDenied("You cannot deactivate your own account.")
        instance.is_active = False
        instance.save()

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class CountyViewSet(viewsets.ModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'county_id']

class SubcountyViewSet(viewsets.ModelViewSet):
    queryset = Subcounty.objects.all()
    serializer_class = SubcountySerializer
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'subcounty_id', 'county__name']

class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = wardSerializers
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'ward_id', 'subcounty__name']

class WardDetailsViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = wardDetailSerializers
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['ward_id']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CropCategorySerializer
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializers
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'crop_id', 'category__name']

class CropVarietyViewSet(viewsets.ModelViewSet):
    queryset = CropVariety.objects.all()
    serializer_class = CropVarietySerializers
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['variety', 'crop__name']

class SoilTypeViewSet(viewsets.ModelViewSet):
    queryset = SoilType.objects.all()
    serializer_class = SoilTypeSerializer
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'texture', 'fertility']


class CropSoilTypeViewSet(viewsets.ModelViewSet):
    queryset = CropSoiltype.objects.all()
    serializer_class = CropSoilTypeSerializer
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['soil_type', 'drainage', 'depth_or_texture']

class AezZoneViewSet(viewsets.ModelViewSet):
    queryset = Aez_zone.objects.all()
    serializer_class = AezSerializers
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['zone_name', 'aez_id']

class LivestockCategoryViewSet(viewsets.ModelViewSet):
    queryset = LivestockCategory.objects.all()
    serializer_class = LivestockCategorySerializers
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class LivestockViewSet(viewsets.ModelViewSet):
    queryset = Livestock.objects.all()
    serializer_class = LivestockSerializers
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['breed', 'livestockcategory__name', 'aez__zone_name']

class PastureCategoryViewSet(viewsets.ModelViewSet):
    queryset = PastureCategory.objects.all()
    serializer_class = PastureCategorySerializers
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class PastureViewSet(viewsets.ModelViewSet):
    queryset = Pasture.objects.all()
    serializer_class = PastureSerializers
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name']

class PastureVarietyViewSet(viewsets.ModelViewSet):
    queryset = PastureVariety.objects.all()
    serializer_class = PastureVaretySerializers
    permission_classes = [IsAdminICTOrResearcherReadUpdate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'pasture_name__name', 'aez__zone_name']

class DashboardStatsViewSet(viewsets.ViewSet):
    """
    Provides aggregated statistics for the dashboard.
    """

    permission_classes = [IsAdminICTOrResearcherReadUpdate]  # Public GET access

    def list(self, request):
        data = {
            "total_counties": County.objects.count(),
            "total_subcounties": Subcounty.objects.count(),
            "total_wards": Ward.objects.count(),
            "total_crops": Crop.objects.count(),
            "total_varieties": CropVariety.objects.count(),
            "total_soiltypes": SoilType.objects.count(),
            "total_aez_zones": Aez_zone.objects.count(),
            "total_livestock_categories": LivestockCategory.objects.count(),
            "total_livestocks": Livestock.objects.count(),
            "total_pasture_categories": PastureCategory.objects.count(),
            "total_pastures": Pasture.objects.count(),
            "total_pasture_varieties": PastureVariety.objects.count(),
        }

        serializer = DashboardStatsSerializer(data)
        return Response(serializer.data)