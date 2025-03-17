from django.contrib import admin
from .models import Banquet ,Order


from .models import Item

admin.site.register(Item)
admin.site.register(Banquet)
admin.register(Order)