from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'dashboard-stats', DashboardStatsViewSet, basename='dashboard-stats')
router.register(r'counties', CountyViewSet)
router.register(r'subcounties', SubcountyViewSet)
router.register(r'wards', WardViewSet)
router.register(r'warddetails', WardDetailsViewSet)

router.register(r'crop-categories', CategoryViewSet)
router.register(r'crops', CropViewSet)
router.register(r'crop-varieties', CropVarietyViewSet)

router.register(r'soil-types', SoilTypeViewSet)
router.register(r'crop-soil-types', CropSoilTypeViewSet)

router.register(r'aez-zones', AezZoneViewSet)

router.register(r'livestock-categories', LivestockCategoryViewSet)
router.register(r'livestocks', LivestockViewSet)

router.register(r'pasture-categories', PastureCategoryViewSet)
router.register(r'pastures', PastureViewSet)
router.register("users", UserViewSet, basename="users")
router.register(r'market-type', MarketTypeViewSet, basename='market-type')
router.register(r'daily-market-priority', DailyMarketPriorityVarietyViewSet, basename='daily-market-priority')
# PastureVariety is part of Pasture model in kalro_selector database
router.register(r'pasture-varieties', PastureVarietyViewSet)
urlpatterns = router.urls