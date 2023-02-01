import unittest
import requests

class CategoryIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost:5000/categories"

    def test_create_category(self):
        url = self.base_url + "/category"
        data = {"name": "category_test"}
        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["category"]["name"], "category_test")

    def test_get_category(self):
        url = self.base_url + "/category/1"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["category"]["id"], 1)
        self.assertEqual(response.json()["category"]["name"], "category_test")

    def test_update_category(self):
        url = self.base_url + "/category/1"
        data = {"name": "category_test_updated"}
        response = requests.put(url, json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["category"]["id"], 1)
        self.assertEqual(response.json()["category"]["name"], "category_test_updated")

    def test_delete_category(self):
        url = self.base_url + "/category/1"
        response = requests.delete(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Category deleted successfully.")

    def test_get_all_categories(self):
        url = self.base_url + "/categories"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()["categories"]), 0)
