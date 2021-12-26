# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Library Imports
# -----------------------------------------------------------------------------
from typing import Optional, TypeVar, Union, List

# -----------------------------------------------------------------------------
# Type defs
# -----------------------------------------------------------------------------
class missing:
    """Used to represent a value not sent by discord api"""

    def __len__(self):
        return 0

    def __eq__(self, o: object):
        return isinstance(o, missing)

    def __repr__(self) -> str:
        return "Field not sent in discord response"

    def __str__(self) -> str:
        return "Field not sent in discord response"

    def __next__(self):
        raise StopIteration

    def __iter__(self):
        return self


T = TypeVar("T")

optional = Union[T, missing]
"""Represents a field that have a chance to not be sent by discord"""

nullable = Optional[T]
"""Represents a field that can return null (None)"""

snowflake = Union[str, int]
"""Represents a field that is a discord snowflake"""

integer = int
"""Represents a integer field"""

boolean = bool
"""Represents a boolean field"""

string = str
"""Represents a string field"""

# This maybe needs another way to be handled
iso8601_timestamp = string
"""Represents a timestamp field"""

# This maybe needs another way to be handled
unix_timestamp = integer
"""Represents a unix timestamp field"""

array = List[T]
"""Represents a array of given type"""

stringarray = List[str]
"""Represents a array of strings"""

snowflakearray = List[snowflake]
"""Represents a array of snowflakes"""

# -----------------------------------------------------------------------------
# Exports
# -----------------------------------------------------------------------------
__all__ = [
    "missing",
    "optional",
    "nullable",
    "snowflake",
    "iso8601_timestamp",
    "unix_timestamp",
    "integer",
    "boolean",
    "string",
    "array",
    "stringarray",
    "snowflakearray",
]
