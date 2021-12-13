from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.permissions import IsAccountantOrReadOnly
from api.models import (
    Material,
    Supplier,
    Currency,
    MeasurementType,
)
from api.serializers import (
    MaterialSerializer,
    SupplierSerializer,
    CurrencySerializer,
    MeasurementTypeSerializer,
)


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.select_related(
        "accountant",
        "supplier",
        "measurement_type",
        "currency",
    )
    serializer_class = MaterialSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAccountantOrReadOnly,)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class MeasurementTypeViewSet(viewsets.ModelViewSet):
    queryset = MeasurementType.objects.all()
    serializer_class = MeasurementTypeSerializer
