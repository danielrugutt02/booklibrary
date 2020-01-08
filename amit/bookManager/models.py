from django.db import models

# Create your models here.
# is a DataFarm compatambile with models

class Book():
    accessionNo = models.IntegerField()
    copyNo = models.IntegerField()
    title = models.CharField()
    authors = models.CharField()
    coauthors = models.CharField()
    editors = models.CharField()
    illustrators = models.CharField()
    publisher = models.CharField()
    edition = models.IntegerField()
    year = models.IntegerField()
    ISBN = models.IntegerField()
    ISBN13 = models.IntegerField()
    ISSN = models.IntegerField()
    callNo = models.CharField()
    category = models.CharField()
    subject = models.CharField()
    type = models.CharField()
    description = models.CharField()
    tags = models.CharField()
    series = models.CharField()
    branch = models.CharField()
    price = models.IntegerField()
    binding = models.CharField()
    condition = models.CharField()
    location = models.CharField()
    includedMaterials = models.CharField()


