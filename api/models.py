from django.db import models
from django.contrib.auth.models import User


class RawMaterial(models.Model):
    # Core fields
    material_name = models.CharField(max_length=25)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    # Foreign Key Relations
    accountant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    supplier = models.ForeignKey(
        "Supplier",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    measurement_type = models.ForeignKey(
        "MeasurementType",
        on_delete=models.CASCADE,
    )
    currency = models.ForeignKey(
        "Currency",
        on_delete=models.CASCADE,
    )

    # Date fields
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.material_name


class Currency(models.Model):
    code = models.CharField(max_length=3)  # TRY, USD, EUR etc.
    name = models.CharField(max_length=25)  # Turkish Lira, U.S. Dollar etc.

    def __str__(self):
        return self.code


class MeasurementType(models.Model):
    code = models.CharField(max_length=5)  # KG etc.
    name = models.CharField(max_length=20)  # Kilogram etc.

    def __str__(self):
        return self.code


class Supplier(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name
