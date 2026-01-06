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
class WardAdmin(BaseImportExportAdmin):
    pass


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
class CropSoilTypeAdmin(BaseImportExportAdmin):
    pass

@admin.register(CropVariety)
class CropVarietyAdmin(BaseImportExportAdmin):
    pass


# -----------------------
# LIVESTOCK MODELS
# -----------------------
@admin.register(LivestockCategory)
class LivestockCategoryAdmin(BaseImportExportAdmin):
    pass


@admin.register(Livestock)
class LivestockAdmin(BaseImportExportAdmin):
    pass


# -----------------------
# PASTURE MODELS
# -----------------------
@admin.register(PastureCategory)
class PastureCategoryAdmin(BaseImportExportAdmin):
    pass


@admin.register(Pasture)
class PastureAdmin(BaseImportExportAdmin):
    pass


@admin.register(PastureVariety)
class PastureVarietyAdmin(BaseImportExportAdmin):
    pass

admin.site.register(User)