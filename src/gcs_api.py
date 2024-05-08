from google.cloud import storage
import os

class GcsApi:

    def __init__(self):
        # Inizializza il client di Google Cloud Storage
        self.client = storage.Client()

    def check_file_exists(self, bucket_name, file_name):

        # Ottieni il riferimento al bucket
        bucket = self.client.bucket(bucket_name)

        # Verifica se il blob (file) esiste
        blob = bucket.blob(file_name)

        if blob.exists():
            return True
        else:
            return None



if __name__ == '__main__':
    #credentials_path = 'pythongcp_privateKey.json'
    #os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    gcs_api = GcsApi()
    bucket_name = 'bucket_vitali'
    file_name = 'scontrini.csv'
    res = gcs_api.check_file_exists(bucket_name, file_name)
    if res:
        print(f"Il file {file_name} esiste nel bucket {bucket_name}.")
    else:
        print(f"Il file {file_name} non esiste nel bucket {bucket_name}.")