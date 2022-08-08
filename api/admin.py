from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from api.models import (
    Material,
    Currency,
    MeasurementType,
    Supplier,
)

User = get_user_model()


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "total_amount",
        "measurement_value",
        "price",
        "is_approved",
        "created_at",
        "updated_at",
    )
    list_editable = ("is_approved",)
    search_fields = ("name", "sku")
    list_filter = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    "name",
                    "sku",
                    "total_amount",
                    "measurement_value",
                    "price",
                    "extra_notes",
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
        "is_approved",
        "created_at",
        "updated_at",
    )
    list_editable = ("is_approved",)
    search_fields = (
        "name",
        "code",
    )
    list_filter = (
        "name",
        "code",
    )


@admin.register(MeasurementType)
class MeasurementTypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "is_approved",
        "created_at",
        "updated_at",
    )
    list_editable = ("is_approved",)
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
        "is_approved",
        "created_at",
        "updated_at",
    )
    list_editable = ("is_approved",)
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


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = [
        "username",
        "is_active",
        "is_staff",
        "is_superuser",
    ]

    add_fieldsets = (
        (
            "Username and Email",
            {
                "fields": (
                    "username",
                    "email",
                ),
            },
        ),
        (
            "Password",
            {
                "fields": ("password1", "password2"),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_staff", "is_superuser"),
            },
        ),
    )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
