
from modules.orientdb_hu import OrientdbHU
from modules.minio_hu import MinioHU

class StoreHu:


    def __init__(self, media_name : str, local_file_path : str):

        self.document_storage = OrientdbHU(media_name=media_name)
        self.file_storage = MinioHU(local_file_path)


    def update_file(self, local_file_path : str ):
        self.file_storage.store_file(local_file_path)






