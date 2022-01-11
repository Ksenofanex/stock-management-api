from django.contrib.auth import get_user_model

import factory

from api.models import Material, Currency, MeasurementType, Supplier

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class CurrencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Currency

    code = "USD"
    name = "United States Dollar"


class MeasurementTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MeasurementType

    code = "KG"
    name = "Kilogram"


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Supplier

    name = factory.Faker("company")
    phone = factory.Faker("phone_number")
    email = factory.Faker("email")
    address = factory.Faker("address")


class MaterialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Material

    accountant = factory.SubFactory(UserFactory)
    currency = factory.SubFactory(CurrencyFactory)
    measurement_type = factory.SubFactory(MeasurementTypeFactory)
    supplier = factory.SubFactory(SupplierFactory)
