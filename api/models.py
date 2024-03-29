from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class BaseAbstractModel(models.Model):
    is_approved = models.BooleanField(
        verbose_name="is approved?", default=False
    )  # Must be approved via admin to be visible in API.

    # Date fields.
    created_at = models.DateTimeField(
        verbose_name="created date", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="updated date", auto_now=True, blank=True
    )

    class Meta:
        abstract = True


class Material(BaseAbstractModel):
    name = models.CharField(verbose_name="material name", max_length=25)
    sku = models.CharField(
        verbose_name="stock keeping unit",
        max_length=50,
        unique=True,
        help_text="Unique identifier for this material.",
    )
    total_amount = models.DecimalField(
        verbose_name="total amount",
        max_digits=9,
        decimal_places=2,
        help_text="Total amount of material to stock.",
    )
    measurement_value = models.DecimalField(
        verbose_name="measurement value",
        max_digits=9,
        decimal_places=2,
        help_text=(
            "If the selected Measurement Type is KG, then setting this value "
            " to 1.87 means 1.87 KG."
        ),
    )
    price = models.DecimalField(
        verbose_name="price", max_digits=9, decimal_places=2
    )
    extra_notes = models.TextField(verbose_name="extra notes", blank=True)

    # ForeignKey relations.
    accountant = models.ForeignKey(
        to=User,
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
    measurement_type = models.ForeignKey(
        to="api.MeasurementType",
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

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"

    def __str__(self):
        return self.name


class Currency(BaseAbstractModel):
    code = models.CharField(
        verbose_name="code",
        max_length=3,
        unique=True,
        help_text="USD, EUR etc.",
    )
    name = models.CharField(
        verbose_name="name",
        max_length=25,
        unique=True,
        help_text="United States Dollar, Euro etc.",
    )

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self):
        return self.code


class MeasurementType(BaseAbstractModel):
    code = models.CharField(
        verbose_name="code",
        max_length=5,
        unique=True,
        help_text="KG, L etc.",
    )
    name = models.CharField(
        verbose_name="name",
        max_length=20,
        unique=True,
        help_text="Kilogram, Litre etc.",
    )

    class Meta:
        verbose_name = "Measurement Type"
        verbose_name_plural = "Measurement Types"

    def __str__(self):
        return self.code


class Supplier(BaseAbstractModel):
    name = models.CharField(verbose_name="name", max_length=30)
    phone = PhoneNumberField(
        verbose_name="phone",
        help_text=(
            "Must be a proper phone number, including country code. "
            "I.e.: +905051111111"
        ),
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
