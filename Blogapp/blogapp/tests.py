from django.test import TestCase

# Create your tests here.
Class Tests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/Blog/')
        self.assertEqual(response.status_code, 200)

    def test_update_page_status_code(self):
        response = self.client.get('/Blog/<int:id>/update/')
        self.assertEqual(response.status_code, 200)


    def test_create_page_status_code(self):
    response = self.client.get('/Blog/<int:id>/create/')
    self.assertEqual(response.status_code, 200)


