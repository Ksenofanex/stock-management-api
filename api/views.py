from rest_framework import generics

from api.permissions import IsAuthorOrReadOnly
from api.models import RawMaterial, Supplier, Currency, MeasurementType
from api.serializers import (
    MaterialSerializer,
    SupplierSerializer,
    CurrencySerializer,
    MeasurementSerializer,
)


class MaterialList(generics.ListCreateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = MaterialSerializer

    def perform_create(self, serializer):  # For setting the author field
        # currently logged-in user.
        serializer.validated_data["accountant"] = self.request.user
        return super(MaterialList, self).perform_create(serializer)


class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = RawMaterial.objects.all()
    serializer_class = MaterialSerializer


class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrencyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class MeasurementList(generics.ListCreateAPIView):
    queryset = MeasurementType.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MeasurementType.objects.all()
    serializer_class = MeasurementSerializer
