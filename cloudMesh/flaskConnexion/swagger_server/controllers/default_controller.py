import connexion
import six

from swagger_server.models.database import Database  # noqa: E501
from swagger_server import util
from db_stub import get_database


def db_get():  # noqa: E501
    """db_get

    Returns timestamp information of the file # noqa: E501


    :rtype: Database
    """
    print get_database()
    return Database(get_database())
