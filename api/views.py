from rest_framework import viewsets

from api.permissions import IsAuthorOrReadOnly
from api.models import RawMaterial, Supplier, Currency, MeasurementType
from api.serializers import (
    MaterialSerializer,
    SupplierSerializer,
    CurrencySerializer,
    MeasurementSerializer,
)


class MaterialListViewSet(viewsets.ModelViewSet):
    queryset = RawMaterial.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = MaterialSerializer

    def perform_create(self, serializer):  # For setting the author field
        # currently logged-in user.
        serializer.validated_data["accountant"] = self.request.user
        return super().perform_create(serializer)


class SupplierListViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CurrencyListViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class MeasurementListViewSet(viewsets.ModelViewSet):
    queryset = MeasurementType.objects.all()
    serializer_class = MeasurementSerializer
