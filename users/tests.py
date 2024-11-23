from django.test import TestCase
from django.contrib.auth import get_user_model

class UsersTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@company.com",
            password="test123"  # This automatically hashes the password
        )

    def test_user_creation(self):
        user = get_user_model().objects.get(id=1)

        self.assertEqual(user.is_staff, False)  # Verify the user is not a staff member by default
        self.assertEqual(self.user.username, user.username)  # Compare usernames
