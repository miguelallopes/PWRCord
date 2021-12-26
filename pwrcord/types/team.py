# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Library Level Imports
# -----------------------------------------------------------------------------
from typing import Dict, Union
from .typings.api import *
from .user import User
from . import PWRCordType


# -----------------------------------------------------------------------------
# Team
# -----------------------------------------------------------------------------


class MembershipState:
    Invited: int = 1
    Accepted: int = 2


class TeamMember(PWRCordType):
    _fields_mapper = ["user", "team_id", "membership_state", "permissions"]

    user: User
    """the avatar, discriminator, id, and username of the user"""
    team_id: snowflake
    """the id of the parent team of which they are a member"""
    membership_state: Union[int, MembershipState]
    """the user's membership state on the team"""
    permissions: array[string] = ["*"]
    """will always be ["*"]"""

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


class Team(PWRCordType):
    _fields_mapper = ["name", "owner_user_id", "id", "members", "icon"]

    name: string
    """the name of the team"""
    owner_user_id: snowflake
    """the user id of the current team owner"""
    id: snowflake
    """the unique id of the team"""
    members: array[TeamMember]
    """the members of the team"""
    icon: nullable[string] = None
    """a hash of the image of the team's icon"""

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

                if field == "members":
                    if object_initialized.__getattr__(field) == missing:
                        object_initialized.__setattr__(field, [])
                    object_initialized.__getattr__(field).append(
                        TeamMember.initialize_json(d)
                    )
                    continue

            object_initialized.__setattr__(field, d)

        return object_initialized
