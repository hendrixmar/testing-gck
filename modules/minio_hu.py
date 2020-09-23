from minio import Minio
from config.config import minio_config
import logging
import uuid
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

class MinioHU(Minio):


    def __init__(self, local_file_path : str):

        super().__init__(minio_config['host'],
                         access_key=minio_config['access_key'],
                         secret_key=minio_config['secret_key'],
                         secure=False)

        self._bucket_name = minio_config['bucket_name']
        folder_name = uuid.uuid4().__str__()
        file_name = uuid.uuid4().__str__()
        self._file_name = f"{folder_name}/{file_name}"

        self.store_file(local_file_path)

    def store_file(self, local_file_path : str):

        try:

            self.fput_object(self.__bucket_name, self._file_name, local_file_path)
        except ResponseError as err:
            logging.warning(err)



    def retrieve_file(self, local_file_path : str):

        try:
            self.fget_object(self.__bucket_name, self._file_name,  local_file_path)
        except ResponseError as err:
            logging.warning(err)

    def delete_file(self):

        self.remove_object(self.__bucket_name, self._file_name)

    def set_bucket_name(self, bucket_name : str):

        self.__bucket_name = bucket_name

