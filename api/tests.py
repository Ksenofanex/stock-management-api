from django.test import TestCase
from django.contrib.auth.models import User

from api.models import (
    Material,
    MeasurementType,
    Supplier,
    Currency,
)


class MaterialTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username="testuser1", password="deneme123"
        )
        measurement_type = MeasurementType.objects.create(
            code="KG", name="Kilogram"
        )
        supplier = Supplier.objects.create(
            name="Tesla",
            phone=123,
            email="tesla@tesla.com",
            address="San Francisco-California-USA",
        )
        currency = Currency.objects.create(
            code="USD", name="United States Dollar"
        )
        Material.objects.create(
            accountant=testuser1,
            name="Tesla Model 3",
            measurement_type=measurement_type,
            measurement_value=1650,
            total_amount=1,
            price=50000.00,
            currency=currency,
            supplier=supplier,
        )

    def test_material(self):
        material = Material.objects.get(id=1)
        accountant = f"{material.accountant}"
        name = f"{material.name}"
        measurement_type = f"{material.measurement_type}"
        measurement_value = f"{material.measurement_value}"
        total_amount = f"{material.total_amount}"
        price = f"{material.price}"
        currency = f"{material.currency}"
        supplier = f"{material.supplier}"

        self.assertEqual(accountant, "testuser1")
        self.assertEqual(name, "Tesla Model 3")
        self.assertEqual(measurement_type, "KG")
        self.assertEqual(measurement_value, "1650.00")
        self.assertEqual(total_amount, "1.00")
        self.assertEqual(price, "50000.00")
        self.assertEqual(currency, "USD")
        self.assertEqual(supplier, "Tesla")
