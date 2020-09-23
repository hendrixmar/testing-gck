from confluent_kafka import Consumer
import youtube_dl
from minio import Minio
from config.config import minio_config
import glob

print("Funcionando")
c = Consumer({
    'bootstrap.servers': '34.83.10.221:9094',
    'group.id': 'test',
    'auto.offset.reset': 'earliest',
    'debug': "consumer, broker, topic",
    "security.protocol": "SSL",
    "ssl.ca.location": 'ca.crt'
})

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

c.subscribe(['test'])
storage = Minio(minio_config['host'],
                         access_key=minio_config['access_key'],
                         secret_key=minio_config['secret_key'],
                         secure=False)


while True:
    try:
        msg = c.poll(1000)

        if msg is None:
            # print("Continue")
            continue
        if msg.error():
            # print("Consumer error: {}".format(msg.error()))
            continue
        else:
            record_key = msg.key()
            record_value = msg.value()
            print(f"{msg.offset()}, Consumed record with key {record_key} and value {record_value}")
            get_audioinfo_from_metadata(msg.value())
            path = glob.glob('*.mp4')[0]
            storage.fput_object("test-datyra", f"youtube/{path}", f"./{path}")

    except:
        print("Exception !!!")

c.close()