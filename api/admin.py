from django.contrib import admin
from .models import RawMaterial, Currency, Supplier, MeasurementType


models = [RawMaterial, Currency, Supplier, MeasurementType]
admin.site.register(models)
