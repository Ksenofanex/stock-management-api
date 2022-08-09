from api.test import StockManagementAPITestCase
from api.tests.factories import (
    CurrencyFactory,
    MeasurementTypeFactory,
    SupplierFactory,
    MaterialFactory,
)
from api.models import Material, Currency, MeasurementType, Supplier


class MaterialViewSetTests(StockManagementAPITestCase):
    def test_if_material_list_page_works(self):
        """Checks if material list page is accessible to all."""
        self.get_check_200(url="v1:material-list")

    def test_if_material_detail_page_works(self):
        """Checks if material detail page is accessible to all."""
        material = MaterialFactory()

        self.get_check_200(url="v1:material-detail", pk=material.id)

    def test_material_list_page_post_permission(self):
        """Checks if unauthenticated user is able to create Material."""
        material_data = {
            "name": "Test Material 1",
            "total_amount": 1.00,
            "measurement_value": 100.00,
            "price": 999.00,
        }

        response = self.post(url_name="v1:material-list", data=material_data)
        self.assert_http_403_forbidden(response=response)

    def test_if_material_list_page_post_works(self):
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

    def test_if_unauthorized_user_can_change_material(self):
        """Checks if unauthorized user (i.e., user that doesn't own material)
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

    def test_if_authorized_user_can_change_material(self):
        """Checks if authorized user (i.e., user that owns material) can
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

    def test_if_unauthorized_user_can_delete_material(self):
        """Checks if unauthorized user (i.e., user that doesn't own material)
        can delete Material."""
        unauthorized_user = self.make_user(username="unauthorized_user")
        material = MaterialFactory()
        url = self.reverse("v1:material-detail", pk=material.id)

        with self.login(unauthorized_user):
            response = self.delete(url_name=url)
            self.assert_http_403_forbidden(response=response)

    def test_if_authorized_user_can_delete_material(self):
        """Checks if authorized user (i.e., user that owns material) can
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
    def test_if_currency_list_page_works(self):
        """Checks if currency list page is accessible to all."""
        self.get_check_200(url="v1:currency-list")

    def test_if_currency_detail_page_works(self):
        """Checks if currency detail page is accessible to all."""
        currency = CurrencyFactory()

        response = self.get(url_name="v1:currency-detail", pk=currency.id)
        self.assert_http_200_ok(response=response)

    def test_currency_list_page_post_permission(self):
        """Checks if unauthenticated user is able to create Currency."""
        currency_data = {
            "code": "ZWL",
            "name": "Zimbabwean Dollar",
        }

        response = self.post(url_name="v1:currency-list", data=currency_data)
        self.assert_http_403_forbidden(response=response)

    def test_if_currency_list_page_post_works(self):
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

    def test_if_currency_is_changeable(self):
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

    def test_if_currency_is_deletable(self):
        """Checks if any authenticated user is allowed to delete Currency."""
        authenticated_user = self.make_user(username="authenticated_user")
        currency = CurrencyFactory()

        with self.login(authenticated_user):
            response = self.delete(
                url_name="v1:currency-detail", pk=currency.id
            )
            self.assert_http_405_method_not_allowed(response=response)


class MeasurementTypeViewSetTests(StockManagementAPITestCase):
    def test_if_measurement_type_list_page_works(self):
        """Checks if measurement type list page is accessible to all."""
        self.get_check_200(url="v1:measurement-type-list")

    def test_if_measurement_type_detail_page_works(self):
        """Checks if measurement type detail page is accessible to all."""
        measurement_type = MeasurementTypeFactory()

        response = self.get(
            url_name="v1:measurement-type-detail", pk=measurement_type.id
        )
        self.assert_http_200_ok(response=response)

    def test_measurement_type_list_page_post_permission(self):
        """Checks if unauthenticated user is able to create MeasurementType."""
        measurement_type_data = {
            "code": "KG",
            "name": "Kilogram",
        }

        response = self.post(
            url_name="v1:measurement-type-list", data=measurement_type_data
        )
        self.assert_http_403_forbidden(response=response)

    def test_if_measurement_type_list_page_post_works(self):
        """Checks if authenticated user is able to create MeasurementType."""
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

    def test_if_measurement_type_is_changeable(self):
        """Checks if any authenticated user is allowed to change
        MeasurementType."""
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

    def test_if_measurement_type_is_deletable(self):
        """Checks if any authenticated user is allowed to delete
        MeasurementType."""
        authenticated_user = self.make_user("authenticated_user")
        measurement_type = MeasurementTypeFactory()

        with self.login(authenticated_user):
            response = self.delete(
                url_name="v1:measurement-type-detail", pk=measurement_type.id
            )
            self.assert_http_405_method_not_allowed(response=response)


class SupplierViewSetTests(StockManagementAPITestCase):
    def test_if_supplier_list_page_works(self):
        """Checks if supplier list page is accessible to all."""
        self.get_check_200(url="v1:supplier-list")

    def test_if_supplier_detail_page_works(self):
        """Checks if supplier detail page is accessible to all."""
        supplier = SupplierFactory()

        response = self.get(url_name="v1:supplier-detail", pk=supplier.id)
        self.assert_http_200_ok(response=response)

    def test_supplier_list_page_post_permission(self):
        """Checks if unauthenticated user is able to create Supplier."""
        supplier_data = {
            "name": "Vought International",
            "phone": "+905051111111",
            "email": "vought@boys.com",
            "address": "Skyscraper, Center Of Evil",
        }

        response = self.post(url_name="v1:supplier-list", data=supplier_data)
        self.assert_http_403_forbidden(response=response)

    def test_if_supplier_list_page_post_works(self):
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

    def test_if_supplier_is_changeable(self):
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

    def test_if_supplier_is_deletable(self):
        """Checks if any authenticated user is allowed to delete Supplier."""
        authenticated_user = self.make_user(username="authenticated_user")
        supplier = SupplierFactory()

        with self.login(authenticated_user):
            response = self.delete(
                url_name="v1:supplier-detail", pk=supplier.id
            )
            self.assert_http_405_method_not_allowed(response=response)
