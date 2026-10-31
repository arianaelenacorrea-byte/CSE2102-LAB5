import unittest
import json
from app import app, subscribers

class PubSubTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        subscribers.clear()

    def test_add_and_list_subscriber(self):
        # Test adding a subscriber
        response = self.client.post('/add-subscriber', 
                                    json={"name": "Grace", "URI": "http://grace.example.com"})
        self.assertEqual(response.status_code, 201)
        
        # Test listing subscribers
        response = self.client.get('/list-subscribers')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("Grace", data)

    def test_delete_subscriber(self):
        subscribers["Ada"] = "http://ada.example.com"
        response = self.client.delete('/delete-subscriber', 
                                      json={"name": "Ada"})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("Ada", subscribers)

    def test_update_subject(self):
        subscribers["Alan"] = "http://example.com"
        response = self.client.post('/update-subject', 
                                    json={"subject-update": "buy IBM"})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()