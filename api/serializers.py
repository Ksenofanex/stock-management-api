from rest_framework import serializers

from api.models import Material, Currency, MeasurementType, Supplier


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = (
            "id",
            "url",
            "code",
            "name",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class MeasurementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementType
        fields = (
            "id",
            "url",
            "code",
            "name",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "url": {
                "view_name": "measurement-type-detail",
                "lookup_field": "pk",
            },
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            "id",
            "url",
            "name",
            "phone",
            "email",
            "address",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class MaterialSerializer(serializers.ModelSerializer):
    supplier_nested = SupplierSerializer(source="supplier", read_only=True)
    measurement_type_nested = MeasurementTypeSerializer(
        source="measurement_type", read_only=True
    )
    currency_nested = CurrencySerializer(source="currency", read_only=True)
    accountant_name = serializers.CharField(
        source="accountant.username", read_only=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtering the objects in the API's Post page's HTML form.
        # If an object isn't approved, it won't be shown in the HTML form of
        # API's Post page.
        self.fields["supplier"].queryset = Supplier.objects.filter(
            is_approved=True
        )
        self.fields[
            "measurement_type"
        ].queryset = MeasurementType.objects.filter(is_approved=True)
        self.fields["currency"].queryset = Currency.objects.filter(
            is_approved=True
        )

    class Meta:
        model = Material
        fields = (
            "id",
            "url",
            "name",
            "sku",
            "created_at",
            "updated_at",
            "accountant_name",
            "measurement_value",
            "measurement_type",
            "measurement_type_nested",
            "total_amount",
            "price",
            "extra_notes",
            "currency",
            "currency_nested",
            "supplier",
            "supplier_nested",
        )
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def create(self, validated_data):
        # For setting the accountant field currently logged-in user.
        validated_data["accountant"] = self.context.get("request").user
        return super().create(validated_data)
