from django.test import TestCase
from django.contrib.auth.models import User

from api.models import RawMaterial, MeasurementType, Supplier, Currency


class MaterialTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='deneme123'
        )
        measurement_type = MeasurementType.objects.create(code='KG', name='Kilogram')
        supplier = Supplier.objects.create(
            name='Tesla', phone=123, email='tesla@tesla.com',
            address='San Francisco-California-USA'
        )
        currency = Currency.objects.create(code='USD', name='United States Dollar')
        test_material = RawMaterial.objects.create(
            accountant=testuser1, material_name='tesla model 3', measurement_type=measurement_type,
            total_amount=1, price=50.00, currency=currency, supplier=supplier
        )

    def test_material(self):
        material = RawMaterial.objects.get(id=1)
        accountant = f"{material.accountant}"
        name = f"{material.material_name}"
        measurement_type = f"{material.measurement_type}"
        total_amount = f"{material.total_amount}"
        price = f"{material.price}"
        currency = f"{material.currency}"
        supplier = f"{material.supplier}"
        
        self.assertEqual(accountant, 'testuser1')
        self.assertEqual(name, 'tesla model 3')
        self.assertEqual(measurement_type, 'KG')
        self.assertEqual(total_amount, '1.00')
        self.assertEqual(price, '50.00')
        self.assertEqual(currency, 'USD')
        self.assertEqual(supplier, 'Tesla')
