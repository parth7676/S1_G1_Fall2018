from django.db import models
from enum import Enum
import datetime
from django.utils import timezone


# Create your models here.
class PropertyCategoryChoices(Enum):
    SingleHouse = 'singleHouse'
    AttachedHouse = 'attachedHouse'
    TownHouse = 'townHouse'
    Apartment = 'apartment'
    Store = 'store'
    Farm = 'farm'
    Factory = 'factory'
    Mall = 'mall'
    Building = 'building'
    Other = 'other'


class PropertySectorChoices(Enum):
    Private = 'private'
    Residential = 'residential'
    Commercial = 'commercial'
    Government = 'government'
    Rural = 'rural'
    Other = 'other'


class PropertyFacingChoices(Enum):
    North = 'north'
    South = 'south'
    East = 'east'
    West = 'west'
    Other = 'other'


class PermissionTypeChoices(Enum):
    Read = 'read'
    Write = 'write'
    Update = 'update'
    Delete = 'delete'


class Country(models.Model):
    def __str__(self):
        return self.countryName

    countryName = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'Countries'


class Province(models.Model):
    def __str__(self):
        return self.provinceName

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinceName = models.CharField(max_length=50)

    class Meta:
        db_table = 'Provinces'


class City(models.Model):
    def __str__(self):
        return self.cityName

    cityName = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province')

    class Meta:
        db_table = 'Cities'


class PropertyCategory(models.Model):
    def __str__(self):
        return self.propertyCategory

    propertyCategory = models.CharField(max_length=100,
                                        choices=[(tag.value, tag.name) for tag in PropertyCategoryChoices],
                                        default=PropertyCategoryChoices.SingleHouse, unique=True)

    class Meta:
        db_table = 'Property_Categories'


class PropertySector(models.Model):
    def __str__(self):
        return self.propertySector

    propertySector = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in PropertySectorChoices],
                                      default=PropertySectorChoices.Commercial, unique=True)

    class Meta:
        db_table = 'Property_Sectors'


class PropertyFacing(models.Model):
    def __str__(self):
        return self.propertyFacing

    propertyFacing = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in PropertyFacingChoices],
                                      default=PropertyFacingChoices.North, unique=True)

    class Meta:
        db_table = 'Property_Facings'


class Property(models.Model):
    def __str__(self):
        return self.propertyTitle

    propertyID = models.AutoField(primary_key=True)
    propertyTitle = models.CharField(max_length=50)
    propertyCategory = models.ForeignKey(PropertyCategory, on_delete=models.SET_NULL, null=True)
    propertySector = models.ForeignKey(PropertySector, on_delete=models.SET_NULL, null=True)
    propertyFacing = models.ForeignKey(PropertyFacing, on_delete=models.SET_NULL, null=True)
    propertyCountry = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    propertyProvince = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    propertyCity = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    propertyStreet = models.CharField(max_length=150)
    propertyStreetNumber = models.CharField(max_length=10)
    propertyPostalCode = models.CharField(max_length=10)
    propertyConstructionDate = models.DateField()
    propertyRegistrationDate = models.DateField()
    propertyNoofHalls = models.IntegerField()
    propertyNoofRooms = models.IntegerField()
    propertyNoofBathrooms = models.FloatField()
    propertyNoofFloors = models.IntegerField()
    propertyTotalArea = models.FloatField()
    propertyAskingPrice = models.FloatField()
    propertySellingPrice = models.FloatField()
    propertyUser = models.ForeignKey(to='User', to_field='userID',
                                        on_delete=models.CASCADE, related_name='user')

    class Meta:
        db_table = 'Properties'


class PropertyImages(models.Model):
    def __str__(self):
        return str(self.property) + "  :  " + str(self.propertyImageId)

    propertyImageId = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    propertyImage = models.ImageField(upload_to='images', max_length=255, null=True, blank=True)
    propertyImageDescription = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'Property_Images'


class User(models.Model):
    def __str__(self):
        return str(self.firstName + " " + self.lastName)

    userID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, null=False)
    lastName = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=30, null=False)
    isActive = models.BooleanField(null=False, default=True)
    last_login = models.DateTimeField(null=True)

    @property
    def full_name(self):
        # "Returns the person's full name."
        return '%s %s' % (self.firstName, self.lastName)

    class Meta:
        db_table = 'Users'


class Password(models.Model):
    def __str__(self):
        return "%s password expires by: %s, Account validity: %s" % (
            self.user, self.passwordMustChanged, self.userAccountExpiryDate)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    encryptedPassword = models.CharField(max_length=255, null=False, default=False)
    salt = models.CharField(max_length=50, null=False, default=False)
    userAccountExpiryDate = models.DateTimeField()
    # "Reset Password after 3 months"
    passwordMustChanged = models.DateTimeField(default=(datetime.datetime.now() + datetime.timedelta(3 * 3565 / 12)),
                                               blank=False)
    passwordReset = models.BooleanField(default=False, blank=False)

    class Meta:
        db_table = 'Passwords'


class RoleCode(models.Model):
    def __str__(self):
        return self.roleName

    roleName = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    class Meta:
        db_table = "Role_Code"


class UserRole(models.Model):
    def __str__(self):
        return self.role.code

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles')
    role = models.ForeignKey(RoleCode, on_delete=models.CASCADE, related_name='role_code')
    dateAssigned = models.DateField(auto_now=True)

    class Meta:
        unique_together = ("user", "role")
        db_table = "User_Role"


class PermissionType(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in PermissionTypeChoices],
                            default=PermissionTypeChoices.Read, unique=True)

    class Meta:
        db_table = 'Permission_Type'


class RolePermission(models.Model):
    def __str__(self):
        return "%s : %s" % (self.code, ', '.join([permission.name for permission in self.permissions.all()]))

    rolePermissionID = models.AutoField(primary_key=True)
    sysFeature = models.CharField(max_length=50)
    code = models.ForeignKey(RoleCode, on_delete=models.CASCADE)
    permissions = models.ManyToManyField(PermissionType)

    class Meta:
        db_table = "Role_Permission"
        ordering = ['rolePermissionID']


class Advertisement(models.Model):
    advID = models.IntegerField(primary_key=True)
    advUserID = models.ForeignKey(to=User, on_delete=models.CASCADE)
    advStartDate = models.DateField()
    advEndDate = models.DateField()
    advDescription = models.CharField(max_length=200)
    propertyID = models.OneToOneField(to=Property, on_delete=models.CASCADE, to_field='propertyID')

    class Meta:
        db_table = "Advertisements"
