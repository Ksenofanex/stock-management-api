from django.urls import path
from .views import \
    (MaterialList,
     MaterialDetail,
     SupplierList,
     SupplierDetail,
     CurrencyList,
     CurrencyDetail,
     MeasurementList,
     MeasurementDetail)


urlpatterns = [
    path('materials/', MaterialList.as_view(), name='api-home'),
    path('materials/<int:pk>/', MaterialDetail.as_view(), name='api-stock-detail'),

    path('suppliers/', SupplierList.as_view(), name='supplier-home'),
    path('suppliers/<int:pk>', SupplierDetail.as_view(), name='api-supplier-detail'),

    path('currencies/', CurrencyList.as_view(), name='currency-home'),
    path('currencies/<int:pk>', CurrencyDetail.as_view(), name='api-currency-detail'),

    path('measurements/', MeasurementList.as_view(), name='measurement-home'),
    path('measurements/<int:pk>', MeasurementDetail.as_view(), name='api-measurement-detail'),
]
