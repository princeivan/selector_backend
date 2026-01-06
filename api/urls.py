from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'counties', CountyViewSet)
router.register(r'subcounties', SubcountyViewSet)
router.register(r'wards', WardViewSet)

router.register(r'categories', CategoryViewSet)
router.register(r'crops', CropViewSet)
router.register(r'crop-varieties', CropVarietyViewSet)

router.register(r'soil-types', SoilTypeViewSet)
router.register(r'soil-conditions', SoilConditionViewSet)

router.register(r'aez-zones', AezZoneViewSet)

router.register(r'livestock-categories', LivestockCategoryViewSet)
router.register(r'livestocks', LivestockViewSet)

router.register(r'pasture-categories', PastureCategoryViewSet)
router.register(r'pastures', PastureViewSet)
router.register(r'pasture-varieties', PastureVarietyViewSet)

urlpatterns = router.urls