from django.contrib import admin

from api.models import (
    RawMaterial,
    Currency,
    Supplier,
    MeasurementType,
)


models = [RawMaterial, Currency, Supplier, MeasurementType]
admin.site.register(models)
