# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Library Level Imports
# -----------------------------------------------------------------------------
from typing import Dict, Union
from dataclasses import dataclass
from .typings.api import *

from .team import Team

from .user import User
from . import PWRCordType

# -----------------------------------------------------------------------------
# Application
# -----------------------------------------------------------------------------
class ApplicationFlag:
    GATEWAY_PRESENCE: int = 1 << 12
    GATEWAY_PRESENCE_LIMITED: int = 1 << 13
    GATEWAY_GUILD_MEMBERS: int = 1 << 14
    GATEWAY_GUILD_MEMBERS_LIMITED: int = 1 << 15
    VERIFICATION_PENDING_GUILD_LIMIT: int = 1 << 16
    EMBEDDED: int = 1 << 17
    GATEWAY_MESSAGE_CONTENT: int = 1 << 18
    GATEWAY_MESSAGE_CONTENT_LIMITED: int = 1 << 19


class Application(PWRCordType):

    _fields_mapper = [
        "id",
        "name",
        "description",
        "bot_public",
        "bot_require_code_grant",
        "summary",
        "verify_key",
        "guild_id",
        "primary_sku_id",
        "team",
        "terms_of_service_url",
        "privacy_policy_url",
        "slug",
        "cover_image",
        "owner",
        "rpc_origins",
        "icon",
        "flags",
    ]

    id: snowflake
    """the id of the app"""
    name: string
    """the name of the app"""
    description: string
    """the description of the app"""

    bot_public: boolean
    """when false only app owner can join the app's bot to guilds"""
    bot_require_code_grant: boolean
    """when true the app's bot will only join upon completion of the full oauth2 code grant flow"""

    summary: string
    """if this application is a game sold on Discord, this field will be the summary field for the store page of its primary sku"""
    verify_key: string
    """the hex encoded key for verification in interactions and the GameSDK's GetTicket"""
    guild_id: optional[snowflake] = missing
    """if this application is a game sold on Discord, this field will be the guild to which it has been linked"""
    primary_sku_id: optional[snowflake] = missing
    """if this application is a game sold on Discord, this field will be the id of the "Game SKU" that is created, if exists"""
    team: optional[Team] = missing
    """if the application belongs to a team, this will be a list of the members of that team"""

    terms_of_service_url: optional[string] = missing
    """the url of the app's terms of service"""
    privacy_policy_url: optional[string] = missing
    """the url of the app's privacy policy"""
    slug: optional[string] = missing
    """if this application is a game sold on Discord, this field will be the URL slug that links to the store page"""
    cover_image: optional[string] = missing
    """the application's default rich presence invite cover image hash"""

    owner: optional[User] = missing
    """partial user object containing info on the owner of the application"""

    rpc_origins: optional[stringarray] = missing
    """an array of rpc origin urls, if rpc is enabled"""

    icon: nullable[string] = None
    """the icon hash of the app"""
    flags: optional[Union[integer, ApplicationFlag]] = missing
    """the application's public flags"""

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
                if field == "owner":
                    d = User.initialize_json(d)

                elif field == "team":
                    d = Team.initialize_json(d)

            object_initialized.__setattr__(field, d)

        return object_initialized
