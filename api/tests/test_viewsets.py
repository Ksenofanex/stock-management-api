from rest_framework import status

from api.test import StockManagementAPITestCase
from api.tests.factories import (
    CurrencyFactory,
    MeasurementTypeFactory,
    SupplierFactory,
)
from api.models import Material


class ViewSetTests(StockManagementAPITestCase):
    def test_if_material_list_page_works(self):
        """Checks if material list page is accessible to all."""
        response = self.get(url_name="material-list")
        assert response.status_code == status.HTTP_200_OK

    def test_if_material_list_page_post_works(self):
        """Checks if authenticated user is able to create Material."""
        test_user = self.make_user("test1")
        currency, measurement_type, supplier = (
            CurrencyFactory(),
            MeasurementTypeFactory(),
            SupplierFactory(),
        )
        material_data = {
            "name": "Test Material 1",
            "total_amount": 1.00,
            "measurement_value": 100.00,
            "price": 999.00,
            "accountant": test_user.id,
            "currency": currency.id,
            "measurement_type": measurement_type.id,
            "supplier": supplier.id,
        }

        with self.login(test_user):
            response = self.post(url_name="material-list", data=material_data)
            assert response.status_code == status.HTTP_201_CREATED

        material = Material.objects.get(id=response.data.get("id"))
        assert material.name == material_data.get("name")
        assert material.total_amount == material_data.get("total_amount")
        assert material.measurement_value == material_data.get(
            "measurement_value"
        )
        assert material.price == material_data.get("price")

    def test_material_list_page_post_permission(self):
        """Checks if unauthenticated user is able to create Material."""
        material_data = {
            "name": "Test Material 1",
            "total_amount": 1.00,
            "measurement_value": 100.00,
            "price": 999.00,
        }

        response = self.post(url_name="material-list", data=material_data)
        assert response.status_code == status.HTTP_403_FORBIDDEN
