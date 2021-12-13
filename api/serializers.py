from rest_framework import serializers

from api.models import Material, Supplier, MeasurementType, Currency


class MeasurementTypeSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="measurement-type-detail", lookup_field="pk"
    )  # Detail page.

    class Meta:
        model = MeasurementType
        fields = (
            "code",
            "name",
            "detail_url",
        )


class CurrencySerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="currency-detail", lookup_field="pk"
    )  # Detail page.

    class Meta:
        model = Currency
        fields = (
            "code",
            "name",
            "detail_url",
        )


class SupplierSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="supplier-detail", lookup_field="pk"
    )  # Detail page.

    class Meta:
        model = Supplier
        fields = (
            "name",
            "phone",
            "email",
            "address",
            "detail_url",
        )


class MaterialSerializer(serializers.ModelSerializer):
    material_url = serializers.HyperlinkedIdentityField(
        view_name="material-detail", lookup_field="pk"
    )  # Detail page.
    supplier_nested = SupplierSerializer(source="supplier", read_only=True)
    measurement_type_nested = MeasurementTypeSerializer(
        source="measurement_type", read_only=True
    )
    currency_nested = CurrencySerializer(source="currency", read_only=True)

    class Meta:
        model = Material
        fields = (
            "id",
            "name",
            "material_url",
            "measurement_type",
            "measurement_value",
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
