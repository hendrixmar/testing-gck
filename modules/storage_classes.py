
from modules.store_hu import StoreHu
import uuid

class S3MediaObject(StoreHu):


    def __init__(self, metadata : dict = {}, local_file_path : str = '', uuid_media : str = '',  uuid : str = None):

        super().__init__(self, 'Media')
        if uuid == None:

            self.metadata = metadata
            self.uuid = uuid.uuid1().hex
            self.uuid_media = uuid_media
            self.local_file_path = local_file_path
            self.minio_file_path = f'{uuid_media}/{self.uuid}'

        else:
            """
                retrieve data
            """
            self.metadata, self._rid = self.retrieve_document(uuid)
            self.local_file_path = self.metadata['local_file_path']
            self.uuid = self.metadata['uuid']
            self.uuid_media = self.metadata['uuid_media']
            self.minio_file_path = self.metadata['minio_file_path']
            self.obtain_file()
            self.downloaded = True
            pass


    def update_metadata(self, metadata : dict):
        """

        :param metadata:
        :return:
        """
        self.metadata = metadata.copy()


    def update_file(self, local_file_path : str ):

        self.update_file(self.file_name, local_file_path)

    def get_metadata(self):
        """

        :return: self.metadata : dict
        """
        return self.metadata

    def get_file(self):
        """

        :return: self.local_file_path : str
        """

        if self.downloaded:
            self.local_file_path
        else:
            raise Exception("File not downloaded")



    def persist_data(self):

        self.metadata.update({
            "uuid" : self.uuid,
            "uuid_media": self.uuid_media,
            "minio_file_path" : self.minio_file_path,

        })
        self.create_file(self.minio_file_path, self.local_file_path)
        temp = self.insert_document(self.metadata)

        return temp



class Media(StoreHu):


    def __init__(self, metadata : dict = {}, local_file_path : str = '', folder_name : str = '',  uuid : str = None):

        super().__init__(self, 'Media')
        if uuid == None:

            self.metadata = metadata
            file_name = uuid.uuid1().hex
            self.file_name = f'{folder_name}/{file_name}'
            self.create_file(self.file_name, local_file_path)
            temp = self.insert_document(metadata)
            self._key = temp

        else:
            """
            retrieve data
            """
            pass


    def update_metadata(self, metadata : dict):
        pass

    def update_file(self, local_file_path : str ):

        self.update_file(self.file_name, local_file_path)

    def update_metadata(self, metadata: dict):
        pass

    def update_file(self, local_file_path: str):
        self.update_file(self.file_name, local_file_path)

    def get_metadata(self):
        """

        :return: self.metadata : dict
        """
        pass

    def get_file(self):
        """

        :return: self.local_file_path : str
        """
        pass

    def persist_data(self):
        pass

        #self.create_file(self.file_name, local_file_path)
        #temp = self.insert_document(self.metadata)





