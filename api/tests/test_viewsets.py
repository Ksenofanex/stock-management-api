from api.test import StockManagementAPITestCase
from api.tests.factories import (
    CurrencyFactory,
    MeasurementTypeFactory,
    SupplierFactory,
    MaterialFactory,
)
from api.models import Material, Currency, MeasurementType, Supplier


class MaterialViewSetTests(StockManagementAPITestCase):
    def test_list_page(self):
        """Checks if Material list page is accessible to all."""
        self.get_check_200(url="v1:material-list")

    def test_detail_page(self):
        """Checks if Material detail page is accessible to all."""
        material = MaterialFactory()

        self.get_check_200(url="v1:material-detail", pk=material.id)

    def test_unauthenticated_user_can_create(self):
        """Checks if unauthenticated user is able to create Material."""
        material_data = {
            "name": "Test Material 1",
            "total_amount": 1.00,
            "measurement_value": 100.00,
            "price": 999.00,
        }

        response = self.post(url_name="v1:material-list", data=material_data)
        self.assert_http_403_forbidden(response=response)

    def test_authenticated_user_can_create(self):
        """Checks if authenticated user is able to create Material."""
        test_user = self.make_user(username="test1")
        currency, measurement_type, supplier = (
            CurrencyFactory(),
            MeasurementTypeFactory(),
            SupplierFactory(),
        )
        material_data = {
            "name": "Test Material 1",
            "sku": "STD-MDL3-TSLA-BLCK-01",
            "total_amount": 1.00,
            "measurement_value": 100.00,
            "price": 999.00,
            "accountant": test_user.id,
            "currency": currency.id,
            "measurement_type": measurement_type.id,
            "supplier": supplier.id,
        }

        with self.login(test_user):
            response = self.post(
                url_name="v1:material-list", data=material_data
            )
            self.assert_http_201_created(response=response)

        material = Material.objects.get(id=response.data.get("id"))
        assert material.name == material_data.get("name")
        assert material.total_amount == material_data.get("total_amount")
        assert material.measurement_value == material_data.get(
            "measurement_value"
        )
        assert material.price == material_data.get("price")
        assert material.accountant == test_user

    def test_unauthorized_user_can_change(self):
        """Checks if unauthorized user (i.e., user that doesn't own Material)
        can change Material."""
        unauthorized_user = self.make_user(username="unauthorized_user")
        material = MaterialFactory()
        material_data = {
            "name": "Changed Material",
            "total_amount": 2.00,
            "measurement_value": 50.00,
            "price": 19.00,
        }

        with self.login(unauthorized_user):
            response = self.put(
                url_name="v1:material-detail",
                pk=material.id,
                data=material_data,
            )
            self.assert_http_403_forbidden(response=response)

    def test_authorized_user_can_change(self):
        """Checks if authorized user (i.e., user that owns Material) can
        change Material."""
        authorized_user = self.make_user(username="authorized_user")
        material = MaterialFactory(accountant=authorized_user)
        material_data = {
            "name": "Changed Material",
            "sku": "TST-SKU-CHNGD-01",
            "total_amount": 2.00,
            "measurement_value": 50.00,
            "price": 19.00,
        }

        with self.login(authorized_user):
            response = self.put(
                url_name="v1:material-detail",
                pk=material.id,
                data=material_data,
            )
            self.assert_http_200_ok(response=response)

        material = Material.objects.get(id=response.data.get("id"))
        assert material.name == material_data.get("name")
        assert material.total_amount == material_data.get("total_amount")
        assert material.measurement_value == material_data.get(
            "measurement_value"
        )
        assert material.price == material_data.get("price")
        assert material.accountant == authorized_user

    def test_unauthorized_user_can_delete(self):
        """Checks if unauthorized user (i.e., user that doesn't own Material)
        can delete Material."""
        unauthorized_user = self.make_user(username="unauthorized_user")
        material = MaterialFactory()

        with self.login(unauthorized_user):
            response = self.delete(
                url_name="v1:material-detail", pk=material.id
            )
            self.assert_http_403_forbidden(response=response)

    def test_authorized_user_can_delete(self):
        """Checks if authorized user (i.e., user that owns Material) can
        delete Material."""
        authorized_user = self.make_user(username="authorized_user")
        material = MaterialFactory(accountant=authorized_user)

        with self.login(authorized_user):
            response = self.delete(
                url_name="v1:material-detail", pk=material.id
            )
            self.assert_http_204_no_content(response=response)

        assert Material.objects.count() == 0


class CurrencyViewSetTests(StockManagementAPITestCase):
    def test_list_page(self):
        """Checks if Currency list page is accessible to all."""
        self.get_check_200(url="v1:currency-list")

    def test_detail_page(self):
        """Checks if Currency detail page is accessible to all."""
        currency = CurrencyFactory()

        response = self.get(url_name="v1:currency-detail", pk=currency.id)
        self.assert_http_200_ok(response=response)

    def test_unauthenticated_user_can_create(self):
        """Checks if unauthenticated user is able to create Currency."""
        currency_data = {
            "code": "ZWL",
            "name": "Zimbabwean Dollar",
        }

        response = self.post(url_name="v1:currency-list", data=currency_data)
        self.assert_http_403_forbidden(response=response)

    def test_authenticated_user_can_create(self):
        """Checks if authenticated user is able to create Currency."""
        test_user = self.make_user(username="test1")
        currency_data = {
            "code": "BTC",
            "name": "Bitcoin",
        }

        with self.login(test_user):
            response = self.post(
                url_name="v1:currency-list", data=currency_data
            )
            self.assert_http_201_created(response=response)

        currency = Currency.objects.get(id=response.data.get("id"))
        assert currency.code == currency_data.get("code")
        assert currency.name == currency_data.get("name")

    def test_authenticated_user_can_change(self):
        """Checks if any authenticated user is allowed to change Currency."""
        authenticated_user = self.make_user(username="authenticated_user")
        currency = CurrencyFactory()
        currency_data = {
            "code": "USDT",
            "name": "Tether",
        }

        with self.login(authenticated_user):
            response = self.put(
                url_name="v1:currency-detail",
                pk=currency.id,
                data=currency_data,
            )
            self.assert_http_405_method_not_allowed(response=response)

    def test_authenticated_user_can_delete(self):
        """Checks if any authenticated user is allowed to delete Currency."""
        authenticated_user = self.make_user(username="authenticated_user")
        currency = CurrencyFactory()

        with self.login(authenticated_user):
            response = self.delete(
                url_name="v1:currency-detail", pk=currency.id
            )
            self.assert_http_405_method_not_allowed(response=response)


class MeasurementTypeViewSetTests(StockManagementAPITestCase):
    def test_list_page(self):
        """Checks if Measurement Type list page is accessible to all."""
        self.get_check_200(url="v1:measurement-type-list")

    def test_detail_page(self):
        """Checks if Measurement Type detail page is accessible to all."""
        measurement_type = MeasurementTypeFactory()

        response = self.get(
            url_name="v1:measurement-type-detail", pk=measurement_type.id
        )
        self.assert_http_200_ok(response=response)

    def test_unauthenticated_user_can_create(self):
        """Checks if unauthenticated user is able to create Measurement
        Type."""
        measurement_type_data = {
            "code": "KG",
            "name": "Kilogram",
        }

        response = self.post(
            url_name="v1:measurement-type-list", data=measurement_type_data
        )
        self.assert_http_403_forbidden(response=response)

    def test_authenticated_user_can_create(self):
        """Checks if authenticated user is able to create Measurement
        Type."""
        test_user = self.make_user(username="test1")
        measurement_type_data = {
            "code": "LB",
            "name": "Pound",
        }

        with self.login(test_user):
            response = self.post(
                url_name="v1:measurement-type-list", data=measurement_type_data
            )
            self.assert_http_201_created(response=response)

        measurement_type = MeasurementType.objects.get(
            id=response.data.get("id")
        )
        assert measurement_type.code == measurement_type_data.get("code")
        assert measurement_type.name == measurement_type_data.get("name")

    def test_authenticated_user_can_change(self):
        """Checks if any authenticated user is allowed to change
        Measurement Type."""
        authenticated_user = self.make_user(username="authenticated_user")
        measurement_type = MeasurementTypeFactory()
        measurement_type_data = {
            "code": "L",
            "name": "Liter",
        }

        with self.login(authenticated_user):
            response = self.put(
                url_name="v1:measurement-type-detail",
                pk=measurement_type.id,
                data=measurement_type_data,
            )
            self.assert_http_405_method_not_allowed(response=response)

    def test_authenticated_user_can_delete(self):
        """Checks if any authenticated user is allowed to delete
        Measurement Type."""
        authenticated_user = self.make_user("authenticated_user")
        measurement_type = MeasurementTypeFactory()

        with self.login(authenticated_user):
            response = self.delete(
                url_name="v1:measurement-type-detail", pk=measurement_type.id
            )
            self.assert_http_405_method_not_allowed(response=response)


class SupplierViewSetTests(StockManagementAPITestCase):
    def test_list_page(self):
        """Checks if Supplier list page is accessible to all."""
        self.get_check_200(url="v1:supplier-list")

    def test_detail_page(self):
        """Checks if Supplier detail page is accessible to all."""
        supplier = SupplierFactory()

        response = self.get(url_name="v1:supplier-detail", pk=supplier.id)
        self.assert_http_200_ok(response=response)

    def test_unauthenticated_user_can_create(self):
        """Checks if unauthenticated user is able to create Supplier."""
        supplier_data = {
            "name": "Vought International",
            "phone": "+905051111111",
            "email": "vought@boys.com",
            "address": "Skyscraper, Center Of Evil",
        }

        response = self.post(url_name="v1:supplier-list", data=supplier_data)
        self.assert_http_403_forbidden(response=response)

    def test_authenticated_user_can_create(self):
        """Checks if authenticated user is able to create Supplier."""
        test_user = self.make_user(username="test1")
        supplier_data = {
            "name": "E Corp",
            "phone": "+905051111111",
            "email": "hack@me.com",
            "address": "Distopia",
        }

        with self.login(test_user):
            response = self.post(
                url_name="v1:supplier-list", data=supplier_data
            )
            self.assert_http_201_created(response=response)

        supplier = Supplier.objects.get(id=response.data.get("id"))
        assert supplier.name == supplier_data.get("name")
        assert supplier.phone == supplier_data.get("phone")
        assert supplier.email == supplier_data.get("email")
        assert supplier.address == supplier_data.get("address")

    def test_authenticated_user_can_change(self):
        """Checks if any authenticated user is allowed to change Supplier."""
        authenticated_user = self.make_user(username="authenticated_user")
        supplier = SupplierFactory()
        supplier_data = {
            "name": "Wayne Enterprise",
            "phone": "+905051111111",
            "email": "richboibruce@thebatman.com",
            "address": "Gotham",
        }

        with self.login(authenticated_user):
            response = self.put(
                url_name="v1:supplier-detail",
                pk=supplier.id,
                data=supplier_data,
            )
            self.assert_http_405_method_not_allowed(response=response)

    def test_authenticated_user_can_delete(self):
        """Checks if any authenticated user is allowed to delete Supplier."""
        authenticated_user = self.make_user(username="authenticated_user")
        supplier = SupplierFactory()

        with self.login(authenticated_user):
            response = self.delete(
                url_name="v1:supplier-detail", pk=supplier.id
            )
            self.assert_http_405_method_not_allowed(response=response)
