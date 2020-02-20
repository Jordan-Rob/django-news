from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.


class HomePageTest(SimpleTestCase):

    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_by_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.htl')


class SignUpPageTest(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_page_status(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_uses_correct_template(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create(
            self.username, self.email
        )
        self.assertEqual()
