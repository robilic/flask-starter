import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password = 'asdf')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password = 'asdf')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password = 'asdf')
        self.assertTrue(u.verify_password('asdf'))
        self.assertFalse(u.verify_password('qwerty'))

    def test_password_salts_are_random(self):
        u1 = User(password = 'asdf')
        u2 = User(password = 'qwerty')
        self.assertTrue(u1.password_hash != u2.password_hash)

