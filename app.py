import logging
import sys
from kafka import KafkaConsumer
import youtube_dl
from minio import Minio
from config.config import minio_config
import glob


LANGUAGUE_CODES = {
    "english" : "en"
}



def get_audioinfo_from_metadata(url : str):
    ydl_opts = {}
    audioinfo = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url)
    audioinfo["title"] = meta.get("title")
    audioinfo["language"] = LANGUAGUE_CODES["english"]
    audioinfo["website"] = meta.get("webpage_url")
    audioinfo["author"] = meta.get("creator")
    audioinfo["episodTitle"] = meta.get("episode")
    audioinfo["audioUrl"] = url
    audioinfo["audioLength"] = meta.get("duration")
    audioinfo["pubDate"] = meta.get("upload_date")
    return audioinfo


storage = Minio(minio_config['host'],
                         access_key=minio_config['access_key'],
                         secret_key=minio_config['secret_key'],
                         secure=False)



root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

#Using Service Name of service(kafka-cluster-kafka-bootstrap.<namespace>.svc:9092)
kafka_consumer = KafkaConsumer(
    'test',
    bootstrap_servers='kafka-cluster-kafka-bootstrap.default.svc:9092',
    group_id=None,
    auto_offset_reset='latest',
    api_version=(0,10)
)

kafka_consumer.poll(timeout_ms=1000)
for msg in kafka_consumer:
    logging.info("====>>>>>: "+str(msg))
    temp = str(msg)
    metadatos = get_audioinfo_from_metadata(temp)
    path = glob.glob('*.mp4')[0]
    storage.fput_object("test-datyra", f"youtube/{path}", f"./{path}")