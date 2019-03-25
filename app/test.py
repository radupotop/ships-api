import unittest
from run import app


class PoleStarTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.testing = True
        cls.test_client = app.test_client()

    def test_get_index(self):
        response = self.test_client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('text/html' in response.content_type)

    def test_get_ships(self):
        response = self.test_client.get('/api/ships/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('application/json' in response.content_type)
        self.assertEqual(len(response.json), 3)

        for ship in response.json:
            self._test_get_positions(ship['imo'])

    def _test_get_positions(self, imo):
        """
        This runs for each ship.
        """
        response = self.test_client.get('/api/positions/{}'.format(imo))
        self.assertEqual(response.status_code, 200)

    def test_bogus_ship_imo(self):
        response = self.test_client.get('/api/positions/123')
        self.assertEqual(response.status_code, 404)

    def test_bogus_ship_imo_notaninteger(self):
        response = self.test_client.get('/api/positions/notaninteger')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main(verbosity=2)
