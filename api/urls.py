from django.urls import path

from api.views import (
    MaterialListViewSet,
    SupplierListViewSet,
    CurrencyListViewSet,
    MeasurementListViewSet,
)

urlpatterns = [
    path(
        "materials/",
        MaterialListViewSet.as_view({"get": "list", "post": "create"}),
        name="stock-list",
    ),
    path(
        "materials/<int:pk>/",
        MaterialListViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="stock-detail",
    ),
    path(
        "suppliers/",
        SupplierListViewSet.as_view({"get": "list", "post": "create"}),
        name="supplier-list",
    ),
    path(
        "suppliers/<int:pk>",
        SupplierListViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="supplier-detail",
    ),
    path(
        "currencies/",
        CurrencyListViewSet.as_view({"get": "list", "post": "create"}),
        name="currency-list",
    ),
    path(
        "currencies/<int:pk>",
        CurrencyListViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="currency-detail",
    ),
    path(
        "measurements/",
        MeasurementListViewSet.as_view({"get": "list", "post": "create"}),
        name="measurement-list",
    ),
    path(
        "measurements/<int:pk>",
        MeasurementListViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="measurement-detail",
    ),
]
