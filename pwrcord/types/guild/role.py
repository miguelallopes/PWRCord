# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Library Imports
# -----------------------------------------------------------------------------
from typing import List
from .. import PWRCordType

# -----------------------------------------------------------------------------
# Module Level Imports
# -----------------------------------------------------------------------------

from ..typings import missing, optional, snowflake, string, boolean, integer


class RoleTag(PWRCordType):

    _fields_mapper: List[str] = ["bot_id", "integration_id", "premium_subscriber"]

    bot_id: optional[snowflake] = missing
    """Bot associated with this role"""
    integration_id: optional[snowflake] = missing
    """Integration associated with this role"""
    premium_subscriber: optional[
        bool
    ] = missing  # TODO Something is wrong in discord docs, I have to analyze this
    """Does this role is a nitro booster server role?"""


class Role(PWRCordType):
    _fields_mapper: List[str] = [
        "id",
        "name",
        "color",
        "hoist",
        "position",
        "permissions",
        "managed",
        "icon",
        "unicode_emoji",
        "mentionable",
        "tags",
    ]

    id: snowflake
    """role id"""

    name: string
    """role name"""

    color: integer
    """integer representation of hexadecimal color code"""

    hoist: boolean
    """Is role pinned in user list?"""

    position: integer
    """hierarchy position of role"""

    permissions: string
    """The permissions of role"""

    managed: string
    """Is this role associated with an integration?"""

    icon: optional[string] = missing
    """Role icon hash"""

    unicode_emoji: optional[string] = missing
    """role unicode emoji"""

    mentionable: boolean = missing
    """Can this role be mentioned"""

    tags: optional[RoleTag] = missing
    """the tags this role has"""

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
                if field == "tags":
                    d = RoleTag.initialize_json(d)

            object_initialized.__setattr__(field, d)

        return object_initialized


__all__ = ["Role" "RoleTag"]
