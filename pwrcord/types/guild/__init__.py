from typing import Union
from ..typings import *
from ..emoji import Emoji
from .. import PWRCordType
from .constants import GuildFeature


class GuildWidget(PWRCordType):
    _fields_mapper = ["enabled", "channel_id"]

    enabled: boolean
    """whether the widget is enabled"""
    channel_id: nullable[snowflake] = None
    """the widget channel id"""


class GuildPreview(PWRCordType):
    _fields_mapper = [
        "id",
        "name",
        "icon",
        "splash",
        "discovery_splash",
        "emojis",
        "features",
        "approximate_member_count",
        "approximate_presence_count",
        "description",
    ]

    id: snowflake
    """guild id"""
    name: string
    """guild name (2-100 characters)"""
    icon: nullable[string] = None
    """icon hash"""
    splash: nullable[string] = None
    """splash hash"""
    discovery_splash: nullable[string] = None
    """discovery splash hash"""
    emojis: array[Emoji]
    """custom guild emojis"""
    features: array[Union[str, GuildFeature]]
    """enabled guild features"""
    approximate_member_count: integer
    """approximate number of members in this guild"""
    approximate_presence_count: integer
    """approximate number of online members in this guild"""
    description: nullable[string] = None
    """the description for the guild, if the guild is discoverable"""

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

            if isinstance(d, list):

                if field == "emojis":
                    if object_initialized.__getattr__(field) == missing:
                        object_initialized.__setattr__(field, [])
                    object_initialized.__getattr__(field).append(
                        Emoji.initialize_json(d)
                    )
                    continue

            object_initialized.__setattr__(field, d)

        return object_initialized
