from rest_framework import serializers

from api.models import RawMaterial, Supplier, MeasurementType, Currency


class MeasurementSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="measurement-detail", lookup_field="pk"
    )  # Detail page.

    class Meta:
        model = MeasurementType
        fields = "__all__"


class CurrencySerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="currency-detail", lookup_field="pk"
    )  # Detail page.

    class Meta:
        model = Currency
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name="supplier-detail", lookup_field="pk"
    )  # Detail page.

    class Meta:
        model = Supplier
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    stock_url = serializers.HyperlinkedIdentityField(
        view_name="stock-detail", lookup_field="pk"
    )  # Detail page.
    supplier_nested = SupplierSerializer(source="supplier", read_only=True)
    measurement_nested = MeasurementSerializer(
        source="measurement_type", read_only=True
    )
    currency_nested = CurrencySerializer(source="currency", read_only=True)

    class Meta:
        model = RawMaterial
        fields = (
            "id",
            "material_name",
            "stock_url",
            "measurement_type",
            "measurement_nested",
            "total_amount",
            "price",
            "currency",
            "currency_nested",
            "created_date",
            "updated_date",
            "supplier",
            "supplier_nested",
        )
