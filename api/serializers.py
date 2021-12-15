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
        )


class MeasurementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementType
        fields = (
            "id",
            "url",
            "code",
            "name",
        )
        extra_kwargs = {
            "url": {
                "view_name": "measurement-type-detail",
                "lookup_field": "pk",
            }
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
        )


class MaterialSerializer(serializers.ModelSerializer):
    supplier_nested = SupplierSerializer(source="supplier", read_only=True)
    measurement_type_nested = MeasurementTypeSerializer(
        source="measurement_type", read_only=True
    )
    currency_nested = CurrencySerializer(source="currency", read_only=True)

    class Meta:
        model = Material
        fields = (
            "id",
            "url",
            "name",
            "measurement_value",
            "measurement_type",
            "measurement_type_nested",
            "total_amount",
            "price",
            "currency",
            "currency_nested",
            "created_date",
            "updated_date",
            "supplier",
            "supplier_nested",
        )

    def create(self, validated_data):
        # For setting the accountant field currently logged-in user.
        validated_data["accountant"] = self.context.get("request").user
        return super().create(validated_data)
