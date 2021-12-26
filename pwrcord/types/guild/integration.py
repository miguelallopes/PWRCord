# -*- coding: utf-8 -*-

from typing import List, Union

# -----------------------------------------------------------------------------
# Module Level Imports
# -----------------------------------------------------------------------------


class IntegrationExpireBehavior:
    RemoveRole: int = 0
    Kick: int = 1


from ..typings import (
    missing,
    nullable,
    iso8601_timestamp,
    optional,
    string,
    integer,
    snowflake,
    boolean,
)
from ..user import User
from .. import PWRCordType


class IntegrationAccount(PWRCordType):

    _fields_mapper: List[str] = ["id", "name"]

    id: string
    """id of the account"""
    name: string
    """name of the account"""


class IntegrationApplication(PWRCordType):
    _fields_mapper: List[str] = ["id", "name", "description", "summary", "icon", "bot"]

    id: string
    """the id of the app"""
    name: string
    """the name of the app"""
    description: string
    """the description of the app"""
    summary: string
    """the summary of the app"""
    icon: nullable[string] = None
    """the icon hash of the app"""
    bot: optional[User] = missing
    """the bot associated with this application"""

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
                if field == "bot":
                    d = User.initialize_json(d)

            object_initialized.__setattr__(field, d)

        return object_initialized


class Integration(PWRCordType):

    _fields_mapper: List[str] = [
        "id",
        "name",
        "type",
        "enabled",
        "account",
        "syncing",
        "role_id",
        "enable_emoticons",
        "expire_behavior",
        "expire_grace_period",
        "user",
        "synced_at",
        "subscriber_count",
        "revoked",
        "application",
    ]

    id: string
    """integration id"""
    name: string
    """integration name"""
    type: string
    """integration type (twitch, youtube, or discord)"""
    enabled: boolean
    """is this integration enabled"""
    account: IntegrationAccount
    """integration account information"""
    syncing: optional[boolean] = missing
    """is this integration syncing"""
    role_id: optional[snowflake] = missing
    """id that this integration uses for 'subscribers'"""
    enable_emoticons: optional[boolean] = missing
    """whether emoticons should be synced for this integration (twitch only currently)"""
    expire_behavior: optional[Union[integer, IntegrationExpireBehavior]] = missing
    """the behavior of expiring subscribers"""
    expire_grace_period: optional[integer] = missing
    """the grace period (in days) before expiring subscribers"""
    user: optional[User] = missing
    """user for this integration"""
    synced_at: optional[iso8601_timestamp] = missing
    """when this integration was last synced"""
    subscriber_count: optional[integer] = missing
    """how many subscribers this integration has"""
    revoked: optional[boolean] = missing
    """has this integration been revoked"""
    application: optional[IntegrationApplication] = missing
    """The bot/OAuth2 application for discord integrations"""

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
                if field == "account":
                    d = IntegrationAccount.initialize_json(d)
                elif field == "user":
                    d = User.initialize_json(d)
                elif field == "application":
                    d = IntegrationApplication.initialize_json(d)

            object_initialized.__setattr__(field, d)

        return object_initialized


__all__ = ["Integration", "IntegrationApplication" "IntegrationAccount"]
