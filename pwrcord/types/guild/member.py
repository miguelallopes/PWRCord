from typing import List
from ..typings import *

from .. import PWRCordType
from ..user import User


class Ban(PWRCordType):

    _fields_mapper: List[str] = ["user", "reason"]
    user: User
    """the banned user"""
    reason: nullable[string] = None
    """the reason for the ban"""

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


class GuildMember(PWRCordType):
    _fields_mapper: List[str] = [
        "user",
        "nick",
        "avatar",
        "roles",
        "joined_at",
        "premium_since",
        "deaf",
        "mute",
        "pending",
        "permissions",
        "communication_disabled_until",
    ]

    user: optional[User] = missing
    """the user this guild member represents"""
    nick: optional[nullable[string]] = missing
    """this user's guild nickname"""
    avatar: optional[nullable[string]] = missing
    """the member's guild avatar hash"""
    roles: snowflakearray
    """array of role object ids"""
    joined_at: iso8601_timestamp
    """when the user joined the guild"""
    premium_since: optional[nullable[iso8601_timestamp]] = missing
    """when the user started boosting the guild"""
    deaf: boolean
    """whether the user is deafened in voice channels"""
    mute: boolean
    """whether the user is muted in voice channels"""
    pending: optional[boolean] = missing
    """whether the user has not yet passed the guild's Membership Screening requirements"""
    permissions: optional[string] = missing
    """total permissions of the member in the channel, including overwrites, returned when in the interaction object"""
    communication_disabled_until = optional[nullable[iso8601_timestamp]] = missing
    """when the user's timeout will expire and the user will be able to communicate in the guild again, null or a time in the past if the user is not timed out"""

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
