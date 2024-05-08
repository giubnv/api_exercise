from google.cloud import bigquery
from google.api_core.exceptions import NotFound
import os

class BigQueryApi:

    def __init__(self):
        self.client = bigquery.Client()

    def exists(self, table_id):
        try:
            self.client.get_table(table_id)
            return True
        except NotFound:
            return None



if __name__ == '__main__':
    #credentials_path = 'pythongcp_privateKey.json'
    #os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    bq_api = BigQueryApi()
    table_id = "training-gcp-309207.dataset_benevento.scontrini"
    res = bq_api.exists(table_id)
    if res:
        print(f"La tabella {table_id} esiste")
    else:
        print(f"La tabella {table_id} non esiste")