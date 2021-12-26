# -*- coding: utf-8 -*-

from typing import List, Union

from .typings.api import *
from . import PWRCordType


class ActivityType:
    Game = 0
    """Playing {name}"""
    Streaming = 1
    """Streaming {details}"""
    Listening = 2
    """Listening to {name}"""
    Watching = 3
    """Watching {name}"""
    Custom = 4
    """{emoji} {name}"""
    Competing = 5
    """Competing in {name}"""


class StatusType:
    Online: str = "online"
    """Online"""

    Idle: str = "idle"
    """AFK"""

    DoNotDisturb: str = "dnd"
    """Do Not Disturb"""

    Invisible: str = "invisible"
    """Invisible and shown as offline"""

    Offline: str = "offline"
    """Offline"""


class ActivityFlag:
    INSTANCE: int = 1 << 0
    JOIN: int = 1 << 1
    SPECTATE: int = 1 << 2
    JOIN_REQUEST: int = 1 << 3
    SYNC: int = 1 << 4
    PLAY: int = 1 << 5
    PARTY_PRIVACY_FRIENDS: int = 1 << 6
    PARTY_PRIVACY_VOICE_CHANNEL: int = 1 << 7
    EMBEDDED: int = 1 << 8


class ActivityTimestamps(PWRCordType):
    _fields_mapper: List[str] = ["start", "end"]

    start: optional[unix_timestamp] = missing
    """unix time (in milliseconds) of when the activity started"""
    end: optional[unix_timestamp] = missing
    """unix time (in milliseconds) of when the activity ends"""


class ActivityEmoji(PWRCordType):
    _fields_mapper: List[str] = ["name", "id", "animated"]

    name: string
    """the name of the emoji"""

    id: optional[snowflake] = missing
    """the id of the emoji"""

    animated: optional[boolean] = False
    """whether this emoji is animated"""


class ActivityParty(PWRCordType):
    _fields_mapper: List[str] = ["id", "size"]

    id: optional[string] = missing
    """the id of the party"""

    size: optional[List[int]] = missing
    """used to show the party's current and maximum size"""


class ActivityAssets(PWRCordType):
    _fields_mapper: List[str] = [
        "large_image",
        "large_text",
        "small_image",
        "small_text",
    ]

    large_image: optional[string] = missing
    """the id for a large asset of the activity, usually a snowflake"""
    large_text: optional[string] = missing
    """text displayed when hovering over the large image of the activity"""
    small_image: optional[string] = missing
    """the id for a small asset of the activity, usually a snowflake"""
    small_text: optional[string] = missing
    """text displayed when hovering over the small image of the activity"""


class ActivitySecrets(PWRCordType):
    _fields_mapper: List[str] = ["join", "spectate", "match"]

    join: optional[string] = missing
    """the secret for joining a party"""
    spectate: optional[string] = missing
    """the secret for spectating a game"""
    match: optional[string] = missing
    """the secret for a specific instanced match"""


class ActivityButton(PWRCordType):
    _fields_mapper: List[str] = ["label", "url"]

    label: string
    """the text shown on the button (1-32 characters)"""

    url: string
    """the url opened when clicking the button (1-512 characters)"""


class Activity(PWRCordType):
    _fields_mapper: List[str] = [
        "name",
        "type",
        "url",
        "created_at",
        "timestamps",
        "application_id",
        "details",
        "state",
        "emoji",
        "party",
        "assets",
        "secrets",
        "instance",
        "flags",
        "buttons",
    ]

    name: string
    """the activity's name"""

    type: Union[int, ActivityType]
    """activity type"""

    url: optional[nullable[string]] = missing
    """stream url, is validated when type is 1 (streaming)"""

    created_at: optional[unix_timestamp] = missing
    """unix timestamp (in milliseconds) of when the activity was added to the user's session"""

    timestamps: optional[ActivityTimestamps] = missing
    """unix timestamps for start and/or end of the game"""

    application_id: optional[snowflake] = missing
    """application id for the game"""

    details: optional[nullable[string]] = missing
    """what the player is currently doing"""

    state: optional[nullable[string]] = missing
    """the user's current party status"""

    emoji: optional[nullable[ActivityEmoji]] = missing
    """the emoji used for a custom status"""

    party: optional[ActivityParty] = missing
    """information for the current party of the player"""

    assets: optional[ActivityAssets] = missing
    """images for the presence and their hover texts"""

    secrets: optional[ActivitySecrets] = missing
    """secrets for Rich Presence joining and spectating"""

    instance: optional[boolean] = missing
    """whether or not the activity is an instanced game session"""

    flags: optional[Union[integer, ActivityFlag]] = missing
    """activity flags OR d together, describes what the payload includes"""

    buttons: optional[array[ActivityButton]] = missing
    """the custom buttons shown in the Rich Presence (max 2)"""

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
                if field == "timestamps":
                    d = ActivityTimestamps.initialize_json(d)
                elif field == "emoji":
                    d = ActivityEmoji.initialize_json(d)
                elif field == "party":
                    d = ActivityParty.initialize_json(d)
                elif field == "assets":
                    d = ActivityAssets.initialize_json(d)
                elif field == "secrets":
                    d = ActivitySecrets.initialize_json(d)

            elif isinstance(d, list):

                if field == "buttons":
                    if object_initialized.__getattr__(field) == missing:
                        object_initialized.__setattr__(field, [])
                    object_initialized.__getattr__(field).append(
                        ActivityButton.initialize_json(d)
                    )
                    continue

            object_initialized.__setattr__(field, d)

        return object_initialized

    @classmethod
    def CreateBotActivity(
        cls,
        name: string,
        type: Union[int, ActivityType] = ActivityType.Game,
        url: optional[nullable[string]] = missing,
    ):

        return cls.initialize_json({"name": name, "type": type, "url": url})


__all__ = [
    "ActivityTimestamps",
    "ActivityEmoji",
    "ActivityType",
    "ActivityFlag",
    "ActivityAssets",
    "ActivityParty",
    "ActivitySecrets",
    "ActivityButton",
    "Activity",
]
