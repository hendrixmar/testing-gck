from pyorient import OrientDB
from config.config import pyorient_config
import json
# DELETE VERTEX Media
class OrientdbHU(OrientDB):


    def __init__(self, media_name : str):

        super().__init__(pyorient_config['host'],
                         pyorient_config['port'])

        self.set_session_token(True)
        self.db_open( pyorient_config['db'],
                      pyorient_config['user'],
                      pyorient_config['password'])

        self.__class_name =  media_name


    def create_edge(self, rid_a: str, rid_b: str):
        """ Method to create edge between two vertexes

        Parameters:
            class_name* (str): Class Name of OrientDB
            rid* (str): Record Id
            json (json): Object Json to save on Database
        Returns:
            Result of updating record on database
        """
        query = f"CREATE EDGE FROM {rid_a}  TO {rid_b}"

        return self.command(query)


    def update_rid(self,  rid, json):
        """ Method to Update Class Object

        Parameters:
            class_name* (str): Class Name of OrientDB
            rid* (str): Record Id
            json (json): Object Json to save on Database
        Returns:
            Result of updating record on database
        """
        query = f'UPDATE {self.__class_name} MERGE {json} WHERE @rid={rid}'

        return self.command(query)

    def update_uuid(self,  uuid, json):
        """ Method to Update Class Object

        Parameters:
            class_name* (str): Class Name of OrientDB
            rid* (str): Record Id
            json (json): Object Json to save on Database
        Returns:
            Result of updating record on database
        """

        query = f'UPDATE {self.__class_name} MERGE {json} WHERE uuid == "{uuid}"'

        return self.command(query)

    def delete_rid(self, class_name, rid):
        """ Method to delete record on OrientDB

        Parameters:
            class_name* (str): Class Name of OrientDB
            rid* (str): Record Id to delete
        Returns:
            Result of delete record
        """
        query = f'DELETE VERTEX {self.__class_name} WHERE @rid={rid}'

        return self.command(query)

    def select_uuids(self, uuids):
        """ Method to get records from rids list
        Parameters:
            rids(list): List of rids [#22:1, #22:3]
        Returns:
            Result of query of OrienDB
        """
        query = f"SELECT FROM {self.__class_name} WHERE id IN {uuids}"

        return self.command(query)


    def select_uuid(self, uuid : str):
        """ Method to get records from rids list
        Parameters:
            uuid(str):
        Returns:
            Result of query of OrienDB
        """
        query = f'SELECT FROM {self.__class_name} WHERE uuid == "{uuid}"'

        return self.command(query)

    def create(self,  json : str):
        """ Method to create Class Object

        Parameters:
            class_name* (str): Class Name of OrientDB
            json (json): Object Json to save on Database
        Returns:
            Result of creation on database
        """

        query = f'INSERT INTO {self.__class_name} CONTENT {json}'

        return self.command(query)

    def select_rid(self, rid: str, table_name: str):

        query = f"select * from {table_name}  where @rid={rid}"

        return self.__db.command(query)