from ..typings import nullable, string, snowflake, array, missing
from .. import PWRCordType


class WelcomeScreenChannel:

    _fields_mapper = ["channel_id", "description", "emoji_id", "emoji_name"]

    channel_id: snowflake
    """the channel's id"""
    description: string
    """the description shown for the channel"""
    emoji_id: nullable[snowflake] = None
    """the emoji id, if the emoji is custom"""
    emoji_name: nullable[string] = None
    """the emoji name if custom, the unicode character if standard, or null if no emoji is set"""


class WelcomeScreen:

    _fields_mapper = ["description", "welcome_channels"]

    description: nullable[string] = None
    welcome_channels: array[WelcomeScreenChannel] = []

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

                if field == "welcome_channels":
                    if object_initialized.__getattr__(field) == missing:
                        object_initialized.__setattr__(field, [])
                    object_initialized.__getattr__(field).append(
                        WelcomeScreenChannel.initialize_json(d)
                    )
                    continue

            object_initialized.__setattr__(field, d)

        return object_initialized
