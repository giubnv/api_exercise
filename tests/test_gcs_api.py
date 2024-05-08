import unittest
from unittest.mock import MagicMock, patch
from src.gcs_api import GcsApi  # Replace 'my_module' with the actual module name

class TestGcsApi(unittest.TestCase):

    @patch('google.cloud.storage.Client')
    def test_client(self, mock_client):
        gcs_api = GcsApi()
        mock_client.assert_called_once()

    @patch('google.cloud.storage.Client')
    def test_check_file_exists_file_exists(self, mock_client):
        # Crea istanza della classe GcsApi
        gcs_api = GcsApi()

        # Mock bucket e blob
        mock_bucket = MagicMock()
        mock_blob = MagicMock()
        mock_bucket.blob.return_value = mock_blob
        mock_blob.exists.return_value = True
        mock_client.return_value.bucket.return_value = mock_bucket

        # Chiamata al metodo check_file_exists
        result = gcs_api.check_file_exists('my_bucket', 'my_file.txt')

        # Assert True
        self.assertTrue(result)

    @patch('google.cloud.storage.Client')
    def test_check_file_exists_file_not_exists(self, mock_client):
        # Crea istanza della classe GcsApi
        gcs_api = GcsApi()

        # Mock bucket e blob
        mock_bucket = MagicMock()
        mock_blob = MagicMock()
        mock_bucket.blob.return_value = mock_blob
        mock_blob.exists.return_value = False
        mock_client.return_value.bucket.return_value = mock_bucket

        # Chiamata al metodo check_file_exists
        result = gcs_api.check_file_exists('my_bucket', 'my_file.txt')

        # Assert None
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()