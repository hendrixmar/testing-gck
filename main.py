from config.config import minio_config
from modules.orientdb_hu import OrientdbHU
from modules.minio_hu import MinioHU
from modules.store_hu import StoreHu
from minio import Minio
import pytube
import youtube_dl
import lorem
from modules.storage_classes import S3MediaObject, Media
import json
import os
from lxml import etree
from xmldiff import main, formatting

key = "5af1a06e025f11ebadede454e83239f7"

media_instance = Media(_uuid=key)
print(media_instance.get_metadata())
for s3media_object in media_instance.iterate_s3media():


    print(s3media_object.get_metadata())
    print(s3media_object.get_transcription())

exit()


with open('slices.json') as json_file:
    data = json.load(json_file)

with open('main.json') as json_file:
    main = json.load(json_file)




directory = os.listdir("TK 87 SIAL")

media_instance = Media(main, '1. Summer Lady.mp3')


for metadata, file in zip(data, directory):

    media_instance.add_s3media(metadata, f"TK 87 SIAL/{file}")

for s3media_object in media_instance.iterate_s3media():

    temp = lorem.text()
    s3media_object.store_transcription(temp)

media_instance.persist_data()






"""


import xml.etree.ElementTree as ET


tree_a = ET.parse('a.xml')
tree_b = ET.parse('b.xml')
for elem_a, elem_b in zip(tree_a.iter(), tree_b.iter()):


    if elem_a.tag != elem_b.tag:
        print("-"* 10,"Not same tag name", "-"* 10)
        print(elem_a.tag[26:], elem_b.tag[26:])
    else:
        print("-"* 10,elem_a.tag[26:], "-"* 10)

    if elem_a.text and elem_b.text:
        print("same length: ", len(elem_a.text) == len(elem_b.text))
        print(len(elem_a.text) , len(elem_b.text))
        print((elem_a.text), (elem_b.text))

    elif elem_a.text or elem_b.text:
        print("value not calculated")

    print("-"*40,"\n\n")

"""