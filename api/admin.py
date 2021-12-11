from django.contrib import admin

from api.models import (
    Material,
    Currency,
    Supplier,
    MeasurementType,
)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "total_amount",
        "measurement_value",
        "price",
        "created_date",
        "updated_date",
    )
    search_fields = ("name",)
    list_filter = (
        "created_date",
        "updated_date",
    )
    readonly_fields = (
        "created_date",
        "updated_date",
    )

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    "name",
                    "total_amount",
                    "measurement_value",
                    "price",
                )
            },
        ),
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
    list_display = (
        "name",
        "code",
    )
    search_fields = (
        "name",
        "code",
    )
    list_filter = (
        "name",
        "code",
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "email",
    )
    search_fields = (
        "name",
        "phone",
        "email",
    )
    list_filter = (
        "name",
        "phone",
        "email",
    )


@admin.register(MeasurementType)
class MeasurementTypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
    )
    search_fields = (
        "name",
        "code",
    )
    list_filter = (
        "name",
        "code",
    )
