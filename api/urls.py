from rest_framework.routers import DefaultRouter

from api.viewsets import (
    MaterialViewSet,
    CurrencyViewSet,
    MeasurementTypeViewSet,
    SupplierViewSet,
)

router = DefaultRouter()
router.register("materials", MaterialViewSet, basename="material")
router.register("currencies", CurrencyViewSet, basename="currency")
router.register(
    "measurement-types", MeasurementTypeViewSet, basename="measurement-type"
)
router.register("suppliers", SupplierViewSet, basename="supplier")
