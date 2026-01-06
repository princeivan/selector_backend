from import_export import resources
from .models import *

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
        fields = ('subcounty_id', 'county', 'subcounty_name',)
        skip_unchanged = True
        report_skipped = True