from django.test import TestCase
from django.urls import reverse

class BasicTests(TestCase):
    def test_homepage_status_code(self):
        """
        Test that the homepage returns a 200 status code.
        """
        response = self.client.get(reverse('home'))  # Replace 'home' with your actual homepage URL name
        self.assertEqual(response.status_code, 200)
cd
    def test_csrf_trusted_origins(self):
        """
        Test that CSRF trusted origins are correctly set in settings.
        """
        from django.conf import settings
        self.assertIn('https://repository.jhubafrica.com', settings.CSRF_TRUSTED_ORIGINS)

    def test_login_page_status_code(self):
        """
        Test that the login page returns a 200 status code.
        """
        response = self.client.get(reverse('login_page'))  # Replace 'login' with your actual login URL name
        self.assertEqual(response.status_code, 200)