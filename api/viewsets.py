from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.permissions import IsAccountantOrReadOnly
from api.models import (
    Material,
    Currency,
    MeasurementType,
    Supplier,
)
from api.serializers import (
    MaterialSerializer,
    CurrencySerializer,
    MeasurementTypeSerializer,
    SupplierSerializer,
)
from api.filters import (
    MaterialFilter,
    CurrencyFilter,
    MeasurementTypeFilter,
    SupplierFilter,
)


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.select_related(
        "accountant",
        "supplier",
        "measurement_type",
        "currency",
    )
    serializer_class = MaterialSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAccountantOrReadOnly,
    )
    filterset_class = MaterialFilter
    http_method_names = ["get", "post", "put", "patch", "delete"]


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filterset_class = CurrencyFilter
    http_method_names = [
        "get",
        "post",
    ]


class MeasurementTypeViewSet(viewsets.ModelViewSet):
    queryset = MeasurementType.objects.all()
    serializer_class = MeasurementTypeSerializer
    filterset_class = MeasurementTypeFilter
    http_method_names = [
        "get",
        "post",
    ]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filterset_class = SupplierFilter
    http_method_names = [
        "get",
        "post",
    ]
