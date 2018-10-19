from django.db import models
from enum import Enum

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
    countryID = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinceID = models.ForeignKey(Province, on_delete=models.CASCADE)

class Property_Category(models.Model):
    propertyCategory = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in Property_Category_Choices], default=Property_Category_Choices.SingleHouse)

class Property_Sector(models.Model):
    propertySector = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in Property_Sector_Choices], default=Property_Sector_Choices.Commercial)

class Property_Facing(models.Model):
    propertyFacing = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in Property_Facing_Choices], default=Property_Facing_Choices.North)

class Property(models.Model):
    propertyID = models.AutoField(primary_key=True)
    propertyTitle = models.CharField(max_length=50)
    propertyCategory = models.ForeignKey(Property_Category, on_delete=models.SET_NULL, null= True)
    propertySector = models.ForeignKey(Property_Sector, on_delete=models.SET_NULL, null= True)
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
    propertyID = models.ForeignKey(Property, on_delete=models.CASCADE)
    propertyImage = models.ImageField(upload_to='images', max_length=255, null=True, blank=True)
    propertyImageID = models.CharField(max_length=50)
    propertyImageDescription = models.CharField(max_length=255, null=True, blank=True)






