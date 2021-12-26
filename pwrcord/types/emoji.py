# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Module Level Imports
# -----------------------------------------------------------------------------

from .typings import (
    missing,
    snowflake,
    nullable,
    string,
    optional,
    snowflakearray,
    boolean,
)
from .user import User
from . import PWRCordType


class Emoji(PWRCordType):
    _fields_mapper = [
        "id",
        "name",
        "roles",
        "user",
        "require_colons",
        "managed",
        "animated",
        "available",
    ]

    id: nullable[snowflake] = None
    """emoji id"""
    name: nullable[string] = None
    """emoji name"""
    roles: optional[snowflakearray] = missing
    """roles allowed to use this emojiS"""

    user: optional[User] = missing
    """user that created this emoji"""

    require_colons: optional[boolean] = missing
    """whether this emoji must be wrapped in colons"""
    managed: optional[boolean] = missing
    """whether this emoji is managed"""
    animated: optional[boolean] = missing
    """whether this emoji is animated"""
    available: optional[boolean] = missing
    """whether this emoji can be used, may be false due to loss of Server Boosts"""

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

            if isinstance(d, dict):
                # Probably we are interacting with object fields
                if field == "user":
                    d = User.initialize_json(d)

            object_initialized.__setattr__(field, d)

        return object_initialized
