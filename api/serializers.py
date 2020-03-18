from rest_framework import serializers
from .models import RawMaterial


class MaterialSerializer(serializers.ModelSerializer):
    supplier_name = serializers.ReadOnlyField(source='supplier.name') # Instead of ID's, showing human-friendly names.
    currency_code = serializers.ReadOnlyField(source='currency.currency_code')
    measurement_type_name = serializers.ReadOnlyField(source='measurement_type.code')
    stock_url = serializers.HyperlinkedIdentityField(view_name='api-stock-detail', lookup_field='pk') # Detail page.

    class Meta:
        model = RawMaterial
        fields = ('id', 'material_name', 'stock_url', 'measurement_type_name', 'measurement_type',
                  'total_amount', 'price', 'currency_code', 'currency',
                  'created_date', 'updated_date', 'supplier_name', 'supplier',)