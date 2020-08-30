from django.db import models

# Create your models here.
from beers.utils import image_upload_location
from core.models import CommonInfo


class Company(CommonInfo):
    name = models.CharField('Name', max_length=50)
    tax_number = models.IntegerField('Tax number', unique=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['-name']

    def __str__(self):
        return self.name


class Beer(CommonInfo):
    COLOR_CHOICES = [
        (0, "Unknown"),
        (1, "Pale Lager"),
        (2, "Blonde Ale"),
        (3, "Hefeweizen"),
        (4, "Pale Ale"),
        (5, "IPA"),
        (6, "Amber Ale"),
        (7, "Irish Red Ale"),
        (8, "Brown Ale"),
        (9, "Porter"),
        (10, "Stout"),
    ]

    name = models.CharField('Name', max_length=50)
    abv = models.DecimalField('Alcohol by volume', max_digits=5, decimal_places=2, default=0)
    is_filtered = models.BooleanField('Is filtered?', default=False)
    color = models.PositiveSmallIntegerField("Color", choices=COLOR_CHOICES, default=0)
    image = models.ImageField("Image", blank=True, null=True, upload_to=image_upload_location)
    company = models.ForeignKey(Company, related_name="beers", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Beer"
        verbose_name_plural = "Beers"
        ordering = ['-name']

    def __str__(self):
        return self.name

    @property
    def is_alcoholic(self):
        return self.abv > 0

    def has_more_alcohol_than(self, alcohol):
        return self.abv > alcohol


class SpecialIngredient(CommonInfo):
    name = models.CharField('Name', max_length=50)
    beers = models.ManyToManyField(Beer, blank=True, related_name="special_ingredients")

    class Meta:
        verbose_name = "Special ingredient"
        verbose_name_plural = "Special ingredients"
        ordering = ['-name']

    def __str__(self):
        return self.name
