from django.contrib.auth import get_user_model

import factory

from api.models import Material, Currency, MeasurementType, Supplier

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class CurrencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Currency
        django_get_or_create = (
            "code",
            "name",
        )  # To avoid duplicates.

    code = factory.Faker("currency_code")
    name = factory.Faker("currency_name")
    is_approved = True


class MeasurementTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MeasurementType
        django_get_or_create = (
            "code",
            "name",
        )  # To avoid duplicates.

    code = "KG"
    name = "Kilogram"
    is_approved = True


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Supplier

    name = factory.Faker("company")
    phone = factory.Faker("phone_number")
    email = factory.Faker("email")
    address = factory.Faker("address")
    is_approved = True


class MaterialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Material

    name = "Test Material"
    sku = factory.Faker("bothify", text="????-????-????-####")
    total_amount = factory.Faker(
        "pydecimal",
        left_digits=9,
        right_digits=2,
        min_value=1,
        max_value=100,
        positive=True,
    )
    measurement_value = factory.Faker(
        "pydecimal",
        left_digits=9,
        right_digits=2,
        min_value=1,
        max_value=100,
        positive=True,
    )
    price = factory.Faker(
        "pydecimal",
        left_digits=9,
        right_digits=2,
        min_value=1,
        max_value=100,
        positive=True,
    )
    is_approved = True

    # ForeignKeys
    accountant = factory.SubFactory(UserFactory)
    currency = factory.SubFactory(CurrencyFactory)
    measurement_type = factory.SubFactory(MeasurementTypeFactory)
    supplier = factory.SubFactory(SupplierFactory)
