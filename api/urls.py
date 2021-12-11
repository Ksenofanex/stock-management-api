from django.urls import path

from api.views import (
    MaterialViewSet,
    SupplierViewSet,
    CurrencyViewSet,
    MeasurementTypeViewSet,
)

urlpatterns = [
    path(
        "materials/",
        MaterialViewSet.as_view({"get": "list", "post": "create"}),
        name="material-list",
    ),
    path(
        "materials/<int:pk>/",
        MaterialViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="material-detail",
    ),
    path(
        "suppliers/",
        SupplierViewSet.as_view({"get": "list", "post": "create"}),
        name="supplier-list",
    ),
    path(
        "suppliers/<int:pk>/",
        SupplierViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="supplier-detail",
    ),
    path(
        "currencies/",
        CurrencyViewSet.as_view({"get": "list", "post": "create"}),
        name="currency-list",
    ),
    path(
        "currencies/<int:pk>/",
        CurrencyViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="currency-detail",
    ),
    path(
        "measurement-types/",
        MeasurementTypeViewSet.as_view({"get": "list", "post": "create"}),
        name="measurement-type-list",
    ),
    path(
        "measurement-types/<int:pk>/",
        MeasurementTypeViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="measurement-type-detail",
    ),
]
