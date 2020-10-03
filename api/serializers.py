from rest_framework import serializers
from .models import RawMaterial, Supplier, MeasurementType, Currency


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementType
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    currency_code = serializers.ReadOnlyField(source='currency.currency_code')
    measurement_type_name = serializers.ReadOnlyField(source='measurement_type.code')
    stock_url = serializers.HyperlinkedIdentityField(view_name='api-stock-detail', lookup_field='pk')  # Detail page.
    supplier_nested = SupplierSerializer(source='supplier', read_only=True)

    class Meta:
        model = RawMaterial
        fields = ('id', 'material_name', 'stock_url', 'measurement_type_name', 'measurement_type',
                  'total_amount', 'price', 'currency_code', 'currency',
                  'created_date', 'updated_date', 'supplier', 'supplier_nested',)
