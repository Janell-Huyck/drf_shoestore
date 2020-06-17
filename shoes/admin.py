from django.contrib import admin

from shoes.models import Shoe, ShoeColor, ShoeType, Manufacturer

admin.site.register(Manufacturer)
admin.site.register(Shoe)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)
