from unittest import TestCase

from domain import get_hi_for_users

class TestDomain(TestCase):
    def test_get_hi_for_users_one_hi_success(self):
        # Preparar tu test
        users = [User(name="gml", age=27, is_active=True)]

        # llamada de interes
        result = get_hi_for_users(users, "hi")

        # checar de lo esperado
        self.assertEqual(result, ["hi gml"])

    def test_get_hi_for_users_no_users_expected_value(self):
        # Preparar tu test
        users = []

        # llamada de interes
        result = get_hi_for_users(users, "hi")

        # checar de lo esperado
        self.assertEqual(result, [])

