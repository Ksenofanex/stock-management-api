from api.test import StockManagementAPITestCase
from api.tests.factories import (
    UserFactory,
    CurrencyFactory,
    MeasurementTypeFactory,
    SupplierFactory,
    MaterialFactory,
)


class ModelTests(StockManagementAPITestCase):
    """Creates mock models and checks if they are created successfully."""

    @classmethod
    def setUpTestData(cls):
        cls.test_user = UserFactory(username="test_user_1")
        cls.currency = CurrencyFactory(code="USD", name="United States Dollar")
        cls.measurement_type = MeasurementTypeFactory()
        cls.supplier = SupplierFactory(
            name="Tesla",
            phone="15051111111",
            email="tesla@tesla.com",
            address="San Francisco, California, USA",
        )
        cls.material = MaterialFactory(
            name="Tesla Model 3",
            sku="STD-MDL3-TSLA-BLCK-01",
            total_amount=1.00,
            accountant=cls.test_user,
            measurement_value=1650.00,
            price=50000.00,
            currency=cls.currency,
            measurement_type=cls.measurement_type,
            supplier=cls.supplier,
        )

    def test_material_is_created(self):
        assert self.material.name == "Tesla Model 3"
        assert self.material.sku == "STD-MDL3-TSLA-BLCK-01"
        assert self.material.total_amount == 1.00
        assert self.material.measurement_value == 1650.00
        assert self.material.price == 50000.00
        assert self.material.accountant.username == "test_user_1"

    def test_currency_is_created(self):
        assert self.currency.code == "USD"
        assert self.currency.name == "United States Dollar"

    def test_measurement_type_is_created(self):
        assert self.measurement_type.code == "KG"
        assert self.measurement_type.name == "Kilogram"

    def test_supplier_is_created_(self):
        assert self.supplier.name == "Tesla"
        assert self.supplier.phone == "15051111111"
        assert self.supplier.email == "tesla@tesla.com"
        assert self.supplier.address == "San Francisco, California, USA"
