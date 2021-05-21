from django.contrib import admin
from .models import Category, Brand, CharacteristicType, Characteristic, Product, VariationType, Variation, ProductImage

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CharacteristicType)
admin.site.register(Characteristic)
admin.site.register(Product)
admin.site.register(VariationType)
admin.site.register(Variation)
admin.site.register(ProductImage)
