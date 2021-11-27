from django.urls import path

from api.views import \
    (MaterialList,
     MaterialDetail,
     SupplierList,
     SupplierDetail,
     CurrencyList,
     CurrencyDetail,
     MeasurementList,
     MeasurementDetail)


urlpatterns = [
    path('materials/', MaterialList.as_view(), name='stock-list'),
    path('materials/<int:pk>/', MaterialDetail.as_view(), name='stock-detail'),

    path('suppliers/', SupplierList.as_view(), name='supplier-list'),
    path('suppliers/<int:pk>', SupplierDetail.as_view(), name='supplier-detail'),

    path('currencies/', CurrencyList.as_view(), name='currency-list'),
    path('currencies/<int:pk>', CurrencyDetail.as_view(), name='currency-detail'),

    path('measurements/', MeasurementList.as_view(), name='measurement-list'),
    path('measurements/<int:pk>', MeasurementDetail.as_view(), name='measurement-detail'),
]
