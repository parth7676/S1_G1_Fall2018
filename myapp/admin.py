from django.contrib import admin

# Register your models here.
from myapp.models import *

admin.site.register(Property)
admin.site.register(PropertyCategory)
admin.site.register(PropertySector)
admin.site.register(PropertyFacing)
admin.site.register(PropertyImages)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(User)
admin.site.register(Password)
admin.site.register(RoleCode)
admin.site.register(RolePermission)
admin.site.register(UserRole)
admin.site.register(PermissionType)
