from django.contrib import admin

from api.models import (
    RawMaterial,
    Currency,
    Supplier,
    MeasurementType,
)


@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "material_name",
        "total_amount",
        "price",
        "created_date",
        "updated_date",
    )
    search_fields = ("material_name",)
    list_filter = (
        "created_date",
        "updated_date",
    )
    readonly_fields = (
        "created_date",
        "updated_date",
    )

    fieldsets = (
        ("Main", {"fields": ("material_name", "total_amount", "price")}),
        (
            "Relations",
            {
                "fields": (
                    "accountant",
                    "currency",
                    "measurement_type",
                    "supplier",
                )
            },
        ),
        (
            "Date",
            {
                "fields": (
                    "created_date",
                    "updated_date",
                )
            },
        ),
    )


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("name", "code",)
    search_fields = ("name", "code",)
    list_filter = ("name", "code",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email",)
    search_fields = ("name", "phone", "email",)
    list_filter = ("name", "phone", "email",)


@admin.register(MeasurementType)
class MeasurementTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "code",)
    search_fields = ("name", "code",)
    list_filter = ("name", "code",)
