
from modules.store_hu import StoreHu
import uuid as uuid_generator
import os

get_extension = lambda path : os.path.splitext(path)[1]

class S3MediaObject(StoreHu):


    def __init__(self, metadata : dict = {}, local_file_path : str = '', uuid_media : str = '',  _uuid : str = None):

        super().__init__('Media')
        if _uuid == None:
            if metadata == {} or local_file_path == '' or uuid_media == '':
                raise Exception("You must instance the class with the metadata, local file path, and uuid media")

            self.metadata = metadata.copy()
            self.__uuid = uuid_generator.uuid1().hex
            self.uuid_media = uuid_media
            self.local_file_path = local_file_path
            self.minio_file_path = f'{uuid_media}/{self.__uuid}{get_extension(local_file_path)}'


        else:
            """
                retrieve data
            """
            self.metadata, self._rid = self.retrieve_document(_uuid)
            self.local_file_path = self.metadata['local_file_path']
            self.uuid = self.metadata['uuid']
            self.uuid_media = self.metadata['uuid_media']
            self.minio_file_path = self.metadata['minio_file_path']
            self.obtain_file(self.minio_file_path ,self.local_file_path)
            self.downloaded = True
            self.__update = False



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

    def __init__(self, metadata: dict = {}, local_file_path: str = '', _uuid = None):

        super().__init__('Media')
        if _uuid == None:
            if metadata == {} or local_file_path == '' :
                raise Exception("You must instance the class with the metadata, local file path, and uuid media")

            self.__metadata = metadata.copy()
            self.__uuid = uuid_generator.uuid1().hex
            self.__local_file_path = local_file_path
            self.__minio_file_path = f'{self.__uuid}/{self.__uuid}{get_extension(local_file_path)}'
            self.__s3media_set = []
            self.__uuid_s3media = []
            self.__update = True
        else:
            """
                retrieve data
            """
            self.__metadata, self._rid = self.retrieve_document(_uuid)
            self.__local_file_path = self.__metadata['local_file_path']
            self.__uuid = self.__metadata['uuid']
            self.__minio_file_path = self.__metadata['minio_file_path']
            self.obtain_file(self.__minio_file_path ,self.__local_file_path)
            self.__downloaded = True
            self.__update = False
            self.__uuid_s3media = self.__metadata["uuid_s3media_set"]

    def add_s3media(self, s3media_object : S3MediaObject):

        self.__s3media_set.append(s3media_object)
        self.__uuid_s3media.append(s3media_object.uuid)


    def update_metadata(self, metadata: dict):
        """

        :param metadata:
        :return:
        """
        self.__metadata = metadata

    def update_file(self, local_file_path: str):
        self.__update = True
        self.__local_file_path = local_file_path


    def get_metadata(self) -> dict:
        """

        :return: self.metadata : dict
        """
        return self.__metadata

    def get_file(self) -> str:
        """

        :return: self.local_file_path : str
        """
        if self.__downloaded:
            self.__local_file_path
        else:
            raise Exception("File not downloaded")

    def persist_data(self):

        self.__metadata.update({
            "uuid": self.__uuid,
            "minio_file_path": self.__minio_file_path,
            "uuid_s3media_set" : self.__uuid_s3media,
            "local_file_path" : self.__local_file_path
        })

        if self.__update:
            self.create_file(self.__minio_file_path, self.__local_file_path)

        if self.__downloaded:
            temp = self.update_document(self.__uuid, self.__metadata)
        else:
            temp = self.insert_document(self.__metadata)

        return temp



