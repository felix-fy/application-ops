import minio
import time,datetime

MINIO_CONF = {
    'endpoint': '127.0.0.1:9001',
    'access_key': 'admin',
    'secret_key': 'HzqbOVu@1c',
    'secure': False
}

def latest_minio_find(bucket: str, object: str):
    client = minio.Minio(**MINIO_CONF)
    if not client.bucket_exists(bucket):
        return None
    data = client.get_object(bucket, object)
    return data.data.decode('utf-8')

if __name__=='__main__':
    for i in range(1,10):
        txt = latest_minio_find("testkkkkkk","test/test.txt")
        print (txt)
        time.sleep(1)
        print (i)
