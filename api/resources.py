from import_export import resources, fields
from .models import *
from import_export.widgets import ForeignKeyWidget

class AezZoneResource(resources.ModelResource):
    class Meta:
        model = Aez_zone
        import_id_fields = ('aez_id',)
        fields = ('aez_id', 'zone_name', 'altitude_range', 'average_annual_rainfall')
        skip_unchanged = True
        report_skipped = True

class CropCategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        import_id_fields = ('id',)  
        fields = ('id', 'name',)    
        skip_unchanged = True
        report_skipped = True

class CountyResource(resources.ModelResource):
    class Meta:
        model = County
        import_id_fields = ('county_id',)  
        fields = ('county_id', 'county_name',)    
        skip_unchanged = True
        report_skipped = True

class SubCountyResource(resources.ModelResource):
    class Meta:
        model = Subcounty
        import_id_fields = ('subcounty_id',)
        fields = ('subcounty_id', 'subcounty_name', 'county')
        skip_unchanged = True
        report_skipped = True
class WardResource(resources.ModelResource):
    class Meta:
        model = Ward
        import_id_fields = ('ward_id',)
        fields = (
            'ward_id',
            'ward_name',
            'county',
            'subcounty',
        )
        skip_unchanged = True
        report_skipped = True
class WarddetailsResource(resources.ModelResource):
    class Meta:
        model = Ward
        import_id_fields = ('id',)
        fields = (
            'ward',
            'latitude',
            'longitude',
            'altitude',
            'annual_rain',
            'annual_temp',
            'ke_elev',
            'ke_ph',
            'lr_rain',
            'lr_temp',
            'sr_rain',
            'sr_temp',
        )
        skip_unchanged = True
        report_skipped = True

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        import_id_fields = ('id',)
        fields = ('id','category_name',)
        skip_unchanged = True
        report_skipped = True

class CropResource(resources.ModelResource):
    class Meta:
        model = Crop
        import_id_fields = ('crop_id',)
        fields = (
            'crop_id',
            'crop_name_en',
            'crop_en_sw',
            'crop_scientificname',
            'category',
        )
        skip_unchanged = True
        report_skipped = True


class SoilTypeResource(resources.ModelResource):
    class Meta:
        model = SoilType
        import_id_fields = ('name',)
        fields = ('name', 'description',)
        skip_unchanged = True
        report_skipped = True

class CropVarietyResource(resources.ModelResource):
    class Meta:
        model = CropVariety
        import_id_fields = ('crop', 'variety')
        fields = (
            'crop',
            'variety',
            'minpH',
            'maxpH',
            'minTemp',
            'maxTemp',
            'minPrep',
            'maxPrep',
            'minAlti',
            'maxAlti',
            'drought_tolerant',
            'pest_tolerant',
            'availability',
            'farmer_preference',
        )
        skip_unchanged = True
        report_skipped = True
class CropSoiltypeResource(resources.ModelResource):
    class Meta:
        model = CropSoiltype
        import_id_fields = ('crop_variety', 'soil_type')
        fields = ('crop_variety', 'soil_type',)
        skip_unchanged = True
        report_skipped = True

class LivestockCategoryResource(resources.ModelResource):
    class Meta:
        model = LivestockCategory
        import_id_fields = ('id',)
        fields = ('id', 'name',)
        skip_unchanged = True
        report_skipped = True
class LivestockResource(resources.ModelResource):
    class Meta:
        model = Livestock
        import_id_fields = ('livestock_id',)
        fields = (
            'livestock_id',
            'breed',
            'livestockcategory',
            'aez',
        )
        skip_unchanged = True
        report_skipped = True

class PastureCategoryResource(resources.ModelResource):
    class Meta:
        model = PastureCategory
        import_id_fields = ('id',)
        fields = ('id', 'name',)
        skip_unchanged = True
        report_skipped = True
class PastureResource(resources.ModelResource):
    class Meta:
        model = Pasture
        import_id_fields = ('pasture_id',)
        fields = ('pasture_id', 'name', 'category',)
        skip_unchanged = True
        report_skipped = True

class PastureVarietyResource(resources.ModelResource):
    class Meta:
        model = PastureVariety
        import_id_fields = ('variety_id',)
        fields = (
            'variety_id',
            'name',
            'pasture_name',
            'aez',
        )
        skip_unchanged = True
        report_skipped = True
