from django.contrib import admin
from beers.models import Beer, Company, SpecialIngredient

# Register your models here.

class BeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'abv', 'is_filtered')
    list_filter = ('is_filtered',)
    exclude = ('created_by', 'last_modified_by')

admin.site.register(Beer, BeerAdmin)
admin.site.register(Company)
admin.site.register(SpecialIngredient)