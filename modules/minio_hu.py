from minio import Minio
from config.config import minio_config
import logging
import uuid
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

class MinioHU(Minio):


    def __init__(self):

        super().__init__(minio_config['host'],
                         access_key=minio_config['access_key'],
                         secret_key=minio_config['secret_key'],
                         secure=False)

        self._bucket_name = minio_config['bucket_name']


    def store_file(self, minio_file_path : str, local_file_path : str):

        try:
            self.fput_object(self.__bucket_name, minio_file_path, local_file_path)
        except ResponseError as err:
            logging.warning(err)


    def retrieve_file(self, minio_file_path : str, local_file_path : str):

        try:
            self.fget_object(self.__bucket_name, minio_file_path, local_file_path)
        except ResponseError as err:
            logging.warning(err)

    def delete_file(self, minio_file_path : str):
        try:
            self.remove_object(self.__bucket_name, minio_file_path)
        except ResponseError as err:
            logging.warning(err)


    def set_bucket_name(self, bucket_name : str):

        self.__bucket_name = bucket_name


