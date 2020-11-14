from django.test import TestCase, Client
from django.test import LiveServerTestCase, TestCase, tag
from django.urls import reverse
from selenium import webdriver
from .models import Report

# Create your tests here.
@tag('functional')
class FunctionalTestCase(LiveServerTestCase):
    """Base class for functional test cases with selenium."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Change to another webdriver if desired (and update CI accordingly).
        options = webdriver.chrome.options.Options()
        # These options are needed for CI with Chromium.
        options.headless = True  # Disable GUI.
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.selenium = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

class MainTestCase(TestCase):
    def test_eksistensi_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # You can also use path names instead of explicit paths.
        response = self.client.get(reverse('report:report'))
        self.assertEqual(response.status_code, 200)

    def test_eksistensi_template(self):
        response = Client().get('/reportIssue/')
        html_response = response.content.decode('utf8')
        self.assertIn("Report Problem", html_response)
        self.assertIn("Submit", html_response)

    def test_eksistensi_navbar(self):
        response = Client().get('/reportIssue/')
        html_response = response.content.decode('utf8')
        self.assertIn("Home", html_response)
        self.assertIn("Donate", html_response)
        self.assertIn("Donations", html_response)
        self.assertIn("Testimonies", html_response)
        self.assertIn("Questions", html_response)
        self.assertIn("Reports", html_response)

class MainFunctionalTestCase(FunctionalTestCase):
    def test_root_url_exists(self):
        self.selenium.get(f'{self.live_server_url}/')
        html = self.selenium.find_element_by_tag_name('html')
        self.assertNotIn('not found', html.text.lower())
        self.assertNotIn('error', html.text.lower())
