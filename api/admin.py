from django.contrib import admin
from .models import * 

admin.site.register(Crop)
admin.site.register(County)
admin.site.register(Subcounty)
admin.site.register(Ward)
admin.site.register(Category)
admin.site.register(CropVariety)
admin.site.register(LivestockCategory)
admin.site.register(Livestock)
admin.site.register(PastureCategory)
admin.site.register(Pasture)
admin.site.register(PastureVariety)
admin.site.register(CropRequirement)
