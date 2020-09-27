from config.config import minio_config
from modules.orientdb_hu import OrientdbHU
from modules.minio_hu import MinioHU
from modules.store_hu import StoreHu
from minio import Minio
import pytube
import youtube_dl
from modules.storage_classes import S3MediaObject, Media

from lxml import etree
from xmldiff import main, formatting


key = "c94cab88-2c7a-4ec3-a779-c3509b6b6856"
file_path = "1. Summer Lady.mp3"
metadata  = {"name": "summer emotions", "author": "james bond"}

temp = Media(_uuid="d2695e3800d611ebb711e454e83239f7")
#temp.update_file('02. Sea Line Rie.mp3')
meta = temp.get_metadata()
meta.update({"name": "bruhhhhhhhhhhhh"})
temp.persist_data()

#temp = Media(_uuid="bfeb5efe00d411eba4d8e454e83239f7")

#temp.persist_data()
#example = StoreHu('Media')
#Media()
#S3MediaObject()
#a = example.retrieve_document(key)



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