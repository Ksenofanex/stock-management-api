from rest_framework import viewsets

from api.permissions import IsAccountantOrReadOnly
from api.models import (
    RawMaterial,
    Supplier,
    Currency,
    MeasurementType,
)
from api.serializers import (
    MaterialSerializer,
    SupplierSerializer,
    CurrencySerializer,
    MeasurementSerializer,
)


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = RawMaterial.objects.select_related(
        "supplier",
        "measurement_type",
        "currency",
    )
    permission_classes = (IsAccountantOrReadOnly,)
    serializer_class = MaterialSerializer

    def perform_create(self, serializer):  # For setting the author field
        # currently logged-in user.
        serializer.validated_data["accountant"] = self.request.user
        return super().perform_create(serializer)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = MeasurementType.objects.all()
    serializer_class = MeasurementSerializer
