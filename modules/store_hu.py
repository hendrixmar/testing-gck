
from modules.orientdb_hu import OrientdbHU
from modules.minio_hu import MinioHU

class StoreHu():


    def __init__(self, media_name : str):

        self.document_storage = OrientdbHU(media_name=media_name)
        self.file_storage = MinioHU()

    def update_file(self,file_name : str, local_file_path : str ):
        self.file_storage.store_file(file_name, local_file_path)

    def create_file(self,minio_file_path : str, local_file_path : str ):
        self.file_storage.store_file(minio_file_path, local_file_path)

    def insert_document(self, json: dict):
        temp = str(json)
        query = self.document_storage.create(temp)
        return query[0]._rid


    def retrieve_document(self, uuid: str):

        document = self.document_storage.select_uuid(uuid)[0]
        return document.oRecordData, document._rid

    def update_document(self, uuid, metadata : dict):

        self.document_storage.update_uuid(uuid, metadata)
        return True

    def obtain_file(self, minio_file_path : str, local_file_path : str ):

        self.file_storage.retrieve_file(minio_file_path, local_file_path)
