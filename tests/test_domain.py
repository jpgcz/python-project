from unittest import TestCase

from domain import get_hi_for_users

class TestDomain(TestCase):
    def test_get_hi_for_users(self):
        result = get_hi_for_users(None)
        self.assertEqual(result, None)
