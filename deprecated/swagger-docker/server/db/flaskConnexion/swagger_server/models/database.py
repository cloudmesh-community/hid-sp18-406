# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Database(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, database: str=None):  # noqa: E501
        """Database - a model defined in Swagger

        :param database: The database of this Database.  # noqa: E501
        :type database: str
        """
        self.swagger_types = {
            'database': str
        }

        self.attribute_map = {
            'database': 'database'
        }

        self._database = database

    @classmethod
    def from_dict(cls, dikt) -> 'Database':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Database of this Database.  # noqa: E501
        :rtype: Database
        """
        return util.deserialize_model(dikt, cls)

    @property
    def database(self) -> str:
        """Gets the database of this Database.


        :return: The database of this Database.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database: str):
        """Sets the database of this Database.


        :param database: The database of this Database.
        :type database: str
        """
        if database is None:
            raise ValueError("Invalid value for `database`, must not be `None`")  # noqa: E501

        self._database = database