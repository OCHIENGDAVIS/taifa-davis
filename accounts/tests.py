from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username='will',
            email='will@gmail.com',
            password='test1234'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

        super_user = User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='test1234'
        )
        self.assertEqual(super_user.username, 'admin')
        self.assertEqual(super_user.email, 'admin@gmail.com')
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)



