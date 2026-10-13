import unittest
from app import app


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.headers = {
            "X-API-Key": "swynex-dev-key"
        }

    # Test 1: Home endpoint
    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # Test 2: Protected endpoint without API key
    def test_missing_api_key(self):
        response = self.client.get("/protected")
        self.assertEqual(response.status_code, 401)

    # Test 3: Protected endpoint with correct API key
    def test_valid_api_key(self):
        response = self.client.get(
            "/protected",
            headers=self.headers
        )
        self.assertEqual(response.status_code, 200)

    # Test 4: Valid product
    def test_valid_product(self):
        response = self.client.post(
            "/products",
            headers=self.headers,
            json={
                "name": "Laptop",
                "price": 50000
            }
        )
        self.assertEqual(response.status_code, 201)

    # Test 5: Empty product name
    def test_empty_product_name(self):
        response = self.client.post(
            "/products",
            headers=self.headers,
            json={
                "name": "",
                "price": 50000
            }
        )
        self.assertEqual(response.status_code, 400)

    # Test 6: Negative product price
    def test_negative_price(self):
        response = self.client.post(
            "/products",
            headers=self.headers,
            json={
                "name": "Laptop",
                "price": -100
            }
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()