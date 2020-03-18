from django.urls import path
from .views import MaterialList, MaterialDetailList


urlpatterns = [
    path('', MaterialList.as_view(), name='api-home'),
    path('<int:pk>/', MaterialDetailList.as_view(), name='api-stock-detail'),
]