from django.db import models
from enum import Enum
import datetime


# Create your models here.
class Property_Category_Choices(Enum):
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


class Property_Sector_Choices(Enum):
    Private = 'private'
    Residential = 'residential'
    Commercial = 'commercial'
    Government = 'government'
    Rural = 'rural'
    Other = 'other'


class Property_Facing_Choices(Enum):
    North = 'north'
    South = 'south'
    East = 'east'
    West = 'west'
    Other = 'other'


class Country(models.Model):
    def __str__(self):
        return self.countryName

    countryName = models.CharField(max_length=50)


class Province(models.Model):
    def __str__(self):
        return self.provinceName

    countryID = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinceName = models.CharField(max_length=50)


class City(models.Model):
    def __str__(self):
        return self.cityName

    cityName = models.CharField(max_length=50)
    countryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    provinceID = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province')


class Property_Category(models.Model):
    def __str__(self):
        return self.propertyCategory

    propertyCategory = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in Property_Category_Choices],
                                        default=Property_Category_Choices.SingleHouse, unique=True)


class Property_Sector(models.Model):
    def __str__(self):
        return self.propertySector

    propertySector = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in Property_Sector_Choices],
                                      default=Property_Sector_Choices.Commercial,unique=True)


class Property_Facing(models.Model):
    def __str__(self):
        return self.propertyFacing

    propertyFacing = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in Property_Facing_Choices],
                                      default=Property_Facing_Choices.North, unique=True)


class Property(models.Model):
    def __str__(self):
        return self.propertyTitle

    propertyID = models.AutoField(primary_key=True)
    propertyTitle = models.CharField(max_length=50)
    propertyCategory = models.ForeignKey(Property_Category, on_delete=models.SET_NULL, null=True)
    propertySector = models.ForeignKey(Property_Sector, on_delete=models.SET_NULL, null=True)
    propertyFacing = models.ForeignKey(Property_Facing, on_delete=models.SET_NULL, null=True)
    propertyCountry = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    propertyProvince = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    propertyCity = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    propertyStreet = models.CharField(max_length=150)
    propertyStreetNumber = models.CharField(max_length=10)
    propertyPostalCode = models.CharField(max_length=10)
    propertyConstructionDate = models.DateField()
    propertyRegisterationDate = models.DateField()
    propertyNoofHalls = models.IntegerField()
    propertyNoofRooms = models.IntegerField()
    propertyNoofBathrooms = models.FloatField()
    propertyNoofFloors = models.IntegerField()
    propertyNoofTotalArea = models.FloatField()
    propertyAskingPrice = models.FloatField()
    propertySellingPrice = models.FloatField()


class Property_Images(models.Model):
    def __str__(self):
        return str(self.propertyID)+"  :  "+str(self.propertyImageId)

    propertyID = models.ForeignKey(Property, on_delete=models.CASCADE)
    propertyImageId = models.AutoField(primary_key=True)
    propertyImage = models.ImageField(upload_to='images', max_length=255, null=True, blank=True)
    propertyImageDescription = models.CharField(max_length=255, null=True, blank=True)


class User(models.Model):
    def __str__(self):
        return str(self.firstName + " " + self.lastName)

    userID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, null=False)
    lastName = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=30, null=False)

    @property
    def full_name(self):
        # "Returns the person's full name."
        return '%s %s' % (self.firstName, self.lastName)


class Password(models.Model):
    def __str__(self):
        return "%s password expires by: %s, Account validity: %s" % (self.user, self.passwordMustChanged, self.userAccountExpiryDate)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    encryptedPassword = models.CharField(max_length=255, null=False, default=False)
    salt = models.CharField(max_length=50, null=False, default=False)
    userAccountExpiryDate = models.DateTimeField()
    # "Reset Password after 3 months"
    passwordMustChanged = models.DateTimeField(default=(datetime.datetime.now()+datetime.timedelta(3*3565/12)), blank=False)
    passwordReset = models.BooleanField(default=False, blank=False)


class RoleCode(models.Model):
    roleName = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    class Meta:
        db_table = "Role_Code"


class UserRole (models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleCode, on_delete=models.CASCADE)
    dateAssigned = models.DateField()

    class Meta:
        unique_together = ("user", "role")
        db_table= "User_Role"


class RolePermission(models.Model):
    def __str__(self):
        return "%s can %s" % (self.code, self.sysFeature)

    rolePermissionID = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    sysFeature = models.CharField(max_length=50)
    role = models.ForeignKey(RoleCode, on_delete=models.CASCADE)

    class Meta:
        db_table = "Role_Permission"


class UserPermissions(models.Model):

    def __str__(self):
        return "%s can %s" % (self.code, self.sysFeature)

    userPermissionID = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    sysFeature = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "User_Permission"
