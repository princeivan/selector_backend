from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import * 

from .models import (
    County, Crop, Subcounty, Ward, Category,
    CropVariety, LivestockCategory, Livestock,
    PastureCategory, Pasture, PastureVariety,
     User,CropSoiltype, Aez_zone
)

# -----------------------
# BASE ADMIN (Reusable)
# -----------------------
class BaseImportExportAdmin(ImportExportModelAdmin):
    search_fields = ('name',)   # works for models with `name`
    list_per_page = 50
    show_full_result_count = False


# -----------------------
# LOCATION MODELS
# -----------------------
@admin.register(County)
class CountyAdmin(ImportExportModelAdmin):
    resource_class = CountyResource


@admin.register(Subcounty)
class SubcountyAdmin(ImportExportModelAdmin):
    resource_class = SubCountyResource


@admin.register(Aez_zone)
class AezZoneAdmin(ImportExportModelAdmin):
    resource_class = AezZoneResource


@admin.register(Ward)
class WardAdmin(ImportExportModelAdmin):
    resource_class = WardResource

@admin.register(Warddetails)
class WardDetailsAdmin(ImportExportModelAdmin):
    resource_class = WarddetailsResource

# -----------------------
# CROP MODELS
# -----------------------
@admin.register(Crop)
class CropAdmin(BaseImportExportAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CropCategoryResource


@admin.register(CropSoiltype)
class CropSoilTypeAdmin(ImportExportModelAdmin):
    resource_class = CropSoiltypeResource

@admin.register(CropVariety)
class CropVarietyAdmin(ImportExportModelAdmin):
    resource_class = CropVarietyResource


# -----------------------
# LIVESTOCK MODELS
# -----------------------
@admin.register(LivestockCategory)
class LivestockCategoryAdmin(ImportExportModelAdmin):
    resource_class = LivestockCategoryResource


@admin.register(Livestock)
class LivestockAdmin(ImportExportModelAdmin):
    resource_class=LivestockResource


# -----------------------
# PASTURE MODELS
# -----------------------
@admin.register(PastureCategory)
class PastureCategoryAdmin(ImportExportModelAdmin):
    resource_class= PastureCategoryResource


@admin.register(Pasture)
class PastureAdmin(ImportExportModelAdmin):
    resource_class = PastureResource


@admin.register(PastureVariety)
class PastureVarietyAdmin(ImportExportModelAdmin):
    resource_class = PastureVarietyResource

admin.site.register(User)