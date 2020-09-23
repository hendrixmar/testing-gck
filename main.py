from config.config import minio_config
from modules.orientdb_hu import OrientdbHU
from modules.minio_hu import MinioHU
from minio import Minio
#example = MinioHU()
import pytube
import youtube_dl

#example.store_file('putos/xdxdxd', 'requirements.txt')

"""
example = Minio(minio_config['host'],
                         access_key=minio_config['access_key'],
                         secret_key=minio_config['secret_key'],
                         secure=False)

objects = example.list_objects('test-datyra')
"""

url = 'youtube_extract'
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
    audioinfo["destination"] = meta.get("destination")
    return audioinfo

#video.download()

url = "https://www.youtube.com/watch?v=gjHCpR1FG5A"

#metadata = get_audioinfo_from_metadata(url)
import glob
print(glob.glob('*.mp4'))



#print(video.title)
