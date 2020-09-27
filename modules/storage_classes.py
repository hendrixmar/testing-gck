
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

            self.__metadata = metadata.copy()
            self.__uuid = uuid_generator.uuid1().hex
            self.__uuid_media = uuid_media
            self.__local_file_path = local_file_path
            self.__minio_file_path = f'{uuid_media}/{self.__uuid}{get_extension(local_file_path)}'
            self.__update = True
            self.__downloaded = False


        else:
            """
                retrieve data
            """
            self.__metadata, self._rid = self.retrieve_document(_uuid)
            self.__local_file_path = self.__metadata['local_file_path']
            self.__uuid = self.__metadata['uuid']
            self.__uuid_media = self.__metadata['uuid_media']
            self.__minio_file_path = self.__metadata['minio_file_path']
            self.obtain_file(self.__minio_file_path ,self.__local_file_path)
            self.__downloaded = True
            self.__update = False



    def update_metadata(self, metadata : dict):
        """

        :param metadata:
        :return:
        """

        if 'uuid' in metadata and (metadata['uuid'] != self.__metadata['uuid']  or \
                metadata['uuid_media'] != self.__metadata['uuid_media']):
            raise Exception("Not permitted change uuid or uuid media")

        self.__metadata.update(metadata)


    def update_file(self, local_file_path : str ):
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
            return self.__local_file_path
        else:
            raise Exception("File not downloaded")



    def persist_data(self):

        self.__metadata.update({
            "uuid" : self.__uuid,
            "uuid_media": self.__uuid_media,
            "minio_file_path" : self.__minio_file_path,
            "local_file_path": self.__local_file_path
        })
        if self.__update:
            self.create_file(self.__minio_file_path, self.__local_file_path)

        if self.__downloaded:
            temp = self.update_document(self.__uuid, self.__metadata)
        else:
            temp = self.insert_document(self.__metadata)

        return self.__uuid



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

            self.__uuid_s3media = []
            self.__update = True
            self.__downloaded = False
            self.__s3media_object_set = []
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
            self.__uuid_s3media = []
            self.__s3media_object_set = []
            for key in self.__metadata["s3media_set"]:
                self.add_s3media(_uuid=key)


    def add_s3media(self, metadata : dict = {}, local_file_path : str = '', _uuid = None):
        if _uuid:
            s3media_object = S3MediaObject(_uuid=_uuid)
        else:
            s3media_object = S3MediaObject(metadata, local_file_path, self.__uuid)

        self.__s3media_object_set.append(s3media_object)



    def update_metadata(self, metadata: dict):
        """

        :param metadata:
        :return:
        """
        if metadata['uuid'] != self.__metadata['uuid'] or \
                metadata['uuid_media'] != self.__metadata['uuid_media']:
            raise Exception("Not permitted change uuid or uuid media")

        self.metadata = metadata

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
            return self.__local_file_path
        else:
            raise Exception("File not downloaded")

    def persist_data(self):

        self.__metadata.update({
            "uuid": self.__uuid,
            "minio_file_path": self.__minio_file_path,

            "local_file_path" : self.__local_file_path
        })

        if self.__update:

            self.create_file(self.__minio_file_path, self.__local_file_path)

        if self.__downloaded:
            temp = self.update_document(self.__uuid, self.__metadata)
        else:
            self.__metadata["s3media_set"] = []
            for s3media_object in self.__s3media_object_set:
                temp = s3media_object.persist_data()
                self.__metadata["s3media_set"].append(temp)

            temp = self.insert_document(self.__metadata)

        return temp



