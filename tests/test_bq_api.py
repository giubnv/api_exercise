import unittest
from unittest.mock import MagicMock, patch
from src.bq_api import BigQueryApi
from google.api_core.exceptions import NotFound

class TestBigQueryApi(unittest.TestCase):

    @patch('google.cloud.bigquery.Client')
    def test_client(self, mock_client):
        bq_api = BigQueryApi()
        mock_client.assert_called_once()
    @patch('google.cloud.bigquery.Client')
    def test_exists_table_exists(self, mock_client):
        # Crea istanza della classe BigQueryApi
        bq_api = BigQueryApi()

        # Mock metodo get_table (ritorna una tabella, simulandone l'esistenza)
        mock_table = MagicMock()
        mock_client.return_value.get_table.return_value = mock_table

        # Chiamata al metodo exists
        result = bq_api.exists('my_project.my_dataset.my_table')

        # Assert True
        self.assertTrue(result)

    @patch('google.cloud.bigquery.Client')
    def test_exists_table_not_found(self, mock_client):
        # Crea istanza della classe BigQueryApi
        bq_api = BigQueryApi()

        # Mock metodo get_table per lanciare una NotFound exception
        mock_client.return_value.get_table.side_effect = NotFound('Table not found')

        # Chiamata al metodo exists
        result = bq_api.exists('my_project.my_dataset.my_table')

        # Assert None
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()