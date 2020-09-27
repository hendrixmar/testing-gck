from config.config import minio_config
from modules.orientdb_hu import OrientdbHU
from modules.minio_hu import MinioHU
from modules.store_hu import StoreHu
from minio import Minio
import pytube
import youtube_dl
from modules.storage_classes import S3MediaObject

from lxml import etree
from xmldiff import main, formatting


key = "c94cab88-2c7a-4ec3-a779-c3509b6b6856"
#example = StoreHu('Media')
S3MediaObject()
#a = example.retrieve_document(key)



exit()


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