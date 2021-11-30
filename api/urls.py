from django.urls import path

from api.views import (
    MaterialList,
    SupplierList,
    CurrencyList,
    MeasurementList,
)


urlpatterns = [
    path(
        "materials/",
        MaterialList.as_view({"get": "list", "post": "create"}),
        name="stock-list",
    ),
    path(
        "materials/<int:pk>/",
        MaterialList.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="stock-detail",
    ),
    path(
        "suppliers/",
        SupplierList.as_view({"get": "list", "post": "create"}),
        name="supplier-list",
    ),
    path(
        "suppliers/<int:pk>",
        SupplierList.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="supplier-detail",
    ),
    path(
        "currencies/",
        CurrencyList.as_view({"get": "list", "post": "create"}),
        name="currency-list",
    ),
    path(
        "currencies/<int:pk>",
        CurrencyList.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="currency-detail",
    ),
    path(
        "measurements/",
        MeasurementList.as_view({"get": "list", "post": "create"}),
        name="measurement-list",
    ),
    path(
        "measurements/<int:pk>",
        MeasurementList.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="measurement-detail",
    ),
]
