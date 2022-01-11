from test_plus.test import TestCase as PlusTestCase

from rest_framework.test import APIClient

from api.tests.factories import UserFactory


class StockManagementAPITestCase(PlusTestCase):
    """django-test-plus package's base test class."""

    client_class = APIClient
    user_factory = UserFactory
