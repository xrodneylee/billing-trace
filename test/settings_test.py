import unittest
import json
import requests

class TenantTestCase(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost:5000/setting/tenant"
        self.header = {
            'Content-Type': 'application/json'
            }
        data = {
            "tenant": "mock",
            "client_id": "mockId",
            "client_secret": "mockPasswrod"
        }
        response = requests.post(self.base_url, headers=self.header, json=data)

    def tearDown(self):
        pass

    def test_tenant_post(self):
        data = {
            "tenant": "guanpu",
            "client_id": "id",
            "client_secret": "passwrod"
        }
        response = requests.post(self.base_url, headers=self.header, json=data)

        self.assertEqual(json.loads(response.json())['tenant'], 'guanpu')
        self.assertEqual(json.loads(response.json())['client_id'], 'id')
        self.assertEqual(json.loads(response.json())['client_secret'], 'passwrod')

    def test_tenant_get(self):
        url = self.base_url + "/mock"
        response = requests.get(url, headers=self.header)

        self.assertEqual(json.loads(response.json())['tenant'], 'mock')
        self.assertEqual(json.loads(response.json())['client_id'], 'mockId')
        self.assertEqual(json.loads(response.json())['client_secret'], 'mockPasswrod')

    def test_tenant_put(self):
        pass

    def test_tenant_delete(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
