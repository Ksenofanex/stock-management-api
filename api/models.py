from django.db import models
from django.contrib.auth.models import User


class RawMaterial(models.Model):
    # Core fields
    material_name = models.CharField(
        verbose_name="material name", max_length=25
    )
    total_amount = models.DecimalField(
        verbose_name="total amount", max_digits=9, decimal_places=2
    )
    measurement_value = models.IntegerField(
        verbose_name="measurement value", default=0
    )  # If MeasurementType is KG, setting this to 100 means 100 KG.
    price = models.DecimalField(
        verbose_name="price", max_digits=9, decimal_places=2
    )

    # Foreign Key Relations
    accountant = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="materials",
        related_query_name="material",
    )
    supplier = models.ForeignKey(
        to="api.Supplier",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="materials",
        related_query_name="material",
    )
    measurement_type = models.ForeignKey(
        to="api.MeasurementType",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="materials",
        related_query_name="material",
    )
    currency = models.ForeignKey(
        to="api.Currency",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="materials",
        related_query_name="material",
    )

    # Date fields
    created_date = models.DateTimeField(
        verbose_name="created date", auto_now_add=True
    )
    updated_date = models.DateTimeField(
        verbose_name="updated date", auto_now=True, blank=True
    )

    class Meta:
        verbose_name = "Raw Material"
        verbose_name_plural = "Raw Materials"

    def __str__(self):
        return self.material_name


class Currency(models.Model):
    code = models.CharField(
        verbose_name="code", max_length=3, unique=True
    )  # TRY, USD, EUR etc.
    name = models.CharField(
        verbose_name="name", max_length=25, unique=True
    )  # Turkish Lira, U.S. Dollar etc.

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self):
        return self.code


class MeasurementType(models.Model):
    code = models.CharField(
        verbose_name="code",
        max_length=5,
        unique=True,
    )  # KG, L etc.
    name = models.CharField(
        verbose_name="name",
        max_length=20,
        unique=True,
    )  # Kilogram, Litre etc.

    class Meta:
        verbose_name = "Measurement Type"
        verbose_name_plural = "Measurement Types"

    def __str__(self):
        return self.code


class Supplier(models.Model):
    name = models.CharField(verbose_name="name", max_length=30)
    phone = models.IntegerField(
        verbose_name="phone",
    )
    email = models.EmailField(
        verbose_name="email",
    )
    address = models.TextField(
        verbose_name="address",
    )

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

    def __str__(self):
        return self.name
