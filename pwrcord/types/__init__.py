# -*- coding: utf-8 -*-

"""Discord API Types for python
This submodule provides easy access to discord api types which allows you to
parse and access data in type hinted classes/structures and prepare your 
payload to discord without the stress of opening the discord docs or using
a trial and error strategy.
"""

# PWRCord Types Module Information
__last_update__: str = "2021-12-25T20:46:00"
"""When «pwrcord.types» submodule received the last update"""

# -----------------------------------------------------------------------------
# Library Level Imports
# -----------------------------------------------------------------------------
from typing import Any, Dict, List, Optional

from .typings.api import missing, optional

# -----------------------------------------------------------------------------
# Base PWRCord Type implementation
# -----------------------------------------------------------------------------
class PWRCordType(object):
    _fields_mapper: List[str] = []
    """
    Describes how should be fields mapped during serialization/deserialization (field names)
    (this must be always overriden with the desired values)
    """

    def __getattr__(self, name: str) -> optional[Any]:
        """Gets a attribute content, returning None if it isn't available

        :param name: Name of attribute to access
        :type name: str
        :return: Attribute content if available, else None
        :rtype: Optional[Any]
        """
        if name == "__fields_mapper":
            return self.__fields_mapper
        return self.__dict__.get(name, missing)

    @classmethod
    def initialize_json(cls, data: dict):
        """[summary]

        :param data: [description]
        :type data: dict
        :return: [description]
        :rtype: [type]
        """
        object_initialized = cls()

        # Fill fields with their respective values
        for field in data:
            d = data[field]
            object_initialized.__setattr__(field, d)

        return object_initialized

    @property
    def dict(self) -> Dict[str, Any]:
        """Using the object fields_mapper, convert our object to a dictionary
        (should be overrided for more control if necessary, generally the default is emough)

        :return: The object encoded to a dictionary
        :rtype: Dict
        """
        return_dict = {}

        for field in self._fields_mapper:
            d = self.__getattr__(field)

            if d != missing:
                if isinstance(d, PWRCordType):
                    return_dict[field] = d.dict
                return_dict[field] = d

        return return_dict


# -----------------------------------------------------------------------------
# Module Level Imports
# -----------------------------------------------------------------------------
from . import typings
