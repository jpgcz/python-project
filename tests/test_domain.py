from unittest import TestCase

from src.domain import get_hi_for_users
from src.models.user import User


class TestDomain(TestCase):
    def test_get_hi_for_users_one_hi_success(self):
        # Preparar tu test
        users = [User('gml', 27, True)]

        # llamada de interes
        result = get_hi_for_users(users, "hi", "Hola")

        # checar de lo esperado
        self.assertEqual(result, ['hi', users[0].name])

    def test_get_hi_for_users_without_users(self):
        # Preparar tu test
        users = []

        # llamada de interes
        result = get_hi_for_users(users, "hi", "Hola")

        # checar de lo esperado
        self.assertEqual(result, [])

    def test_get_hi_for_users_no_users_expected_value(self):
        # Preparar tu test
        users = [User('gml', 27, True), User('joce', 26, True), User('jpg', 28, True)]

        # llamada de interes
        result = get_hi_for_users(users, "hi")

        # checar de lo esperado
        self.assertEqual(result, ['hi', users[0].name])
        self.assertEqual(result, ['hi', users[1].name])
        self.assertEqual(result, ['hi', users[2].name])
