import unittest
import json
import requests

class TenantTestCase(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost:5000/setting/tenant"
        self.header = {
            'Content-Type': 'application/json'
            }

        self.data = {
            "tenant": "mock",
            "client_id": "mockId",
            "client_secret": "mockPasswrod"
        }
        response = requests.post(self.base_url, headers=self.header, json=self.data)

    def tearDown(self):
        url = self.base_url + "/mock"
        response = requests.delete(url, headers=self.header)

    def test_tenant_post(self):
        data = {
            "tenant": "mock1",
            "client_id": "mockId",
            "client_secret": "mockPasswrod"
        }
        response = requests.post(self.base_url, headers=self.header, json=data)

        self.assertEqual(json.loads(response.json())['tenant'], 'mock1')
        self.assertEqual(json.loads(response.json())['client_id'], 'mockId')
        self.assertEqual(json.loads(response.json())['client_secret'], 'mockPasswrod')

        url = self.base_url + "/mock1"
        response = requests.delete(url, headers=self.header)

    def test_tenant_get(self):
        url = self.base_url + "/mock"
        response = requests.get(url, headers=self.header)

        self.assertEqual(json.loads(response.json())['tenant'], 'mock')
        self.assertEqual(json.loads(response.json())['client_id'], 'mockId')
        self.assertEqual(json.loads(response.json())['client_secret'], 'mockPasswrod')

    def test_tenant_put(self):
        data = {
            "tenant": "mock",
            "client_id": "modify",
            "client_secret": "modify"
        }
        response = requests.put(self.base_url, headers=self.header, json=data)

        self.assertEqual(json.loads(response.json())['tenant'], 'mock')
        self.assertEqual(json.loads(response.json())['client_id'], 'modify')
        self.assertEqual(json.loads(response.json())['client_secret'], 'modify')

    def test_tenant_delete(self):
        url = self.base_url + "/mock"
        response = requests.delete(url, headers=self.header)
        self.assertFalse(response.json())

if __name__ == '__main__':
    unittest.main(verbosity=2)
