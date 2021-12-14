from django_filters import rest_framework as filters

from api.models import Material, Currency, MeasurementType, Supplier


class MaterialFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )
    currency_code = filters.CharFilter(
        field_name="currency__code",
        lookup_expr="icontains",
    )
    currency_name = filters.CharFilter(
        field_name="currency__name",
        lookup_expr="icontains",
    )
    measurement_type_code = filters.CharFilter(
        field_name="measurement_type__code",
        lookup_expr="icontains",
    )
    measurement_type_name = filters.CharFilter(
        field_name="measurement_type__name",
        lookup_expr="icontains",
    )
    supplier_name = filters.CharFilter(
        field_name="supplier__name",
        lookup_expr="icontains",
    )
    supplier_phone = filters.NumberFilter(
        field_name="supplier__phone",
        lookup_expr="icontains",
    )
    supplier_email = filters.CharFilter(
        field_name="supplier__email",
        lookup_expr="icontains",
    )
    supplier_address = filters.CharFilter(
        field_name="supplier__address",
        lookup_expr="icontains",
    )

    class Meta:
        model = Material
        fields = [
            "name",
            "currency_code",
            "currency_name",
            "measurement_type_code",
            "measurement_type_name",
            "supplier_name",
            "supplier_phone",
            "supplier_email",
            "supplier_address",
        ]


class CurrencyFilter(filters.FilterSet):
    code = filters.CharFilter(
        field_name="code",
        lookup_expr="icontains",
    )
    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = Currency
        fields = [
            "code",
            "name",
        ]


class MeasurementTypeFilter(filters.FilterSet):
    code = filters.CharFilter(
        field_name="code",
        lookup_expr="icontains",
    )
    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = MeasurementType
        fields = [
            "code",
            "name",
        ]


class SupplierFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )
    phone = filters.NumberFilter(
        field_name="phone",
        lookup_expr="icontains",
    )
    email = filters.CharFilter(
        field_name="email",
        lookup_expr="icontains",
    )
    address = filters.CharFilter(
        field_name="address",
        lookup_expr="icontains",
    )

    class Meta:
        model = Supplier
        fields = [
            "name",
            "phone",
            "email",
            "address",
        ]
