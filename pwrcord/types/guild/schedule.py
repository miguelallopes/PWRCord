from typing import List, Union
from ..typings import *

from .. import PWRCordType
from ..user import User
from .member import GuildMember


class GuildScheduledEventPrivacyLevel:
    GUILD_ONLY: int = 2
    """the scheduled event is only accessible to guild members"""


class GuildScheduledEventEntityType:
    STAGE_INSTANCE: int = 1
    VOICE: int = 2
    EXTERNAL: int = 3


class GuildScheduledEventStatus:
    SCHEDULED: int = 1
    ACTIVE: int = 2
    COMPLETED: int = 3
    CANCELED: int = 4


class GuildScheduledEventUser(PWRCordType):
    _fields_mapper: List[str] = ["guild_scheduled_event_id", "user", "member"]

    guild_scheduled_event_id: snowflake
    """the scheduled event id which the user subscribed to"""

    user: User
    """user which subscribed to an event"""

    member: optional[GuildMember] = missing
    """guild member data for this user for the guild which this event belongs to, if any"""

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
                elif field == "member":
                    d = GuildMember.initialize_json(d)

            object_initialized.__setattr__(field, d)

        return object_initialized


class GuildScheduledEventEntityMetadata(PWRCordType):
    _fields_mapper: List[str] = ["location"]

    location: optional[string] = missing
    """location of the event (1-100 characters)"""


class GuildScheduledEvent(PWRCordType):

    _fields_mapper: List[str] = [
        "id",
        "guild_id",
        "channel_id",
        "creator_id",
        "name",
        "description",
        "scheduled_start_time",
        "scheduled_end_time",
        "privacy_level",
        "status",
        "entity_type",
        "entity_id",
        "entity_metadata",
        "creator",
        "user_count",
    ]

    id: snowflake
    """the id of the scheduled event"""
    guild_id: snowflake
    """the guild id which the scheduled event belongs to"""
    channel_id: nullable[snowflake] = None
    """the channel id in which the scheduled event will be hosted, or null if scheduled entity type is EXTERNAL"""
    creator_id: nullable[snowflake] = None
    """the id of the user that created the scheduled event"""
    name: string
    """the name of the scheduled event (1-100 characters)"""
    description: optional[string] = missing
    """the description of the scheduled event (1-1000 characters)"""
    scheduled_start_time: iso8601_timestamp
    """the time the scheduled event will start"""
    scheduled_end_time: nullable[iso8601_timestamp] = None
    """the time the scheduled event will end, required if entity_type is EXTERNAL"""
    privacy_level: Union[int, GuildScheduledEventPrivacyLevel]
    """the privacy level of the scheduled event"""
    status: Union[int, GuildScheduledEventStatus]
    """the status of the scheduled event"""
    entity_type: Union[int, GuildScheduledEventEntityType]
    """the type of the scheduled event"""
    entity_id: nullable[snowflake] = None
    """the id of an entity associated with a guild scheduled event"""
    entity_metadata: nullable[GuildScheduledEventEntityMetadata] = None
    """additional metadata for the guild scheduled event"""
    creator: optional[User] = missing
    """the user that created the scheduled event"""
    user_count: optional[integer] = missing
    """the number of users subscribed to the scheduled event"""

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
                if field == "creator":
                    d = User.initialize_json(d)
                elif field == "entity_metadata":
                    d = GuildScheduledEventEntityMetadata.initialize_json(d)

            object_initialized.__setattr__(field, d)

        return object_initialized
