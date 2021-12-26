from typing import Union

from .typings.api import *
from . import PWRCordType


class UserFlag:
    Null: int = 0
    DiscordEmployee: int = 1 << 0
    PartneredServerOwner: int = 1 << 1
    HypeSquadEvents: int = 1 << 2
    BugHunterLevel1: int = 1 << 3
    HouseBravery: int = 1 << 6
    HouseBrilliance: int = 1 << 7
    HouseBalance: int = 1 << 8
    EarlySupporter: int = 1 << 9
    TeamUser: int = 1 << 10
    BugHunterLevel2: int = 1 << 14
    VerifiedBot: int = 1 << 16
    EarlyVerifiedBotDeveloper: int = 1 << 17
    DiscordCertifiedModerator: int = 1 << 18
    BotHTTPInteractions: int = 1 << 19


class PremiumType:
    Null: int = 0
    NitroClassic: int = 1
    Nitro: int = 2


class User(PWRCordType):
    _fields_mapper = [
        "id",
        "username",
        "discriminator",
        "avatar",
        "bot",
        "system",
        "mfa_enabled",
        "banner",
        "accent_color",
        "locale",
        "verified",
        "verified",
        "email",
        "flags",
        "premium_type",
        "public_flags",
    ]

    id: snowflake
    """the user's id"""

    username: string
    """the user's username, not unique across the platform"""

    discriminator: string
    """the user's username, not unique across the platform"""

    avatar: nullable[string] = None
    """the user's avatar hash"""

    bot: optional[bool] = False
    """whether the user belongs to an OAuth2 application"""

    system: optional[bool] = False
    """whether the user is an Official Discord System user (part of the urgent message system)"""

    mfa_enabled: optional[bool] = missing
    """whether the user has two factor enabled on their account"""

    banner: optional[nullable[string]] = missing
    """the user's banner hash"""

    accent_color: optional[nullable[integer]] = missing
    """the user's banner color encoded as an integer representation of hexadecimal color code"""

    locale: optional[string] = missing
    """the user's chosen language option"""

    verified: optional[boolean] = missing
    """whether the email on this account has been verified"""

    email: optional[nullable[string]] = missing
    """the user's email"""

    flags: optional[Union[int, UserFlag]] = missing
    """the flags on a user's account"""

    premium_type: optional[Union[int, PremiumType]] = missing
    """the type of Nitro subscription on a user's account"""

    public_flags: optional[Union[int, UserFlag]] = missing
    """the public flags on a user's account"""


__all__ = ["User", "PremiumType", "UserFlag"]
