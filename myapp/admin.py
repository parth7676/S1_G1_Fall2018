from django.contrib import admin

# Register your models here.
from myapp.models import Property, Property_Category, Property_Sector, Property_Facing, Property_Images, Country, \
    Province, City

admin.site.register(Property)
admin.site.register(Property_Category)
admin.site.register(Property_Sector)
admin.site.register(Property_Facing)
admin.site.register(Property_Images)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
