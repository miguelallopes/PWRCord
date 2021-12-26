# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Util Variables
# -----------------------------------------------------------------------------
ORJSON_AVAILABLE: bool = False
"""Checks if 'orjson' library is available"""

# -----------------------------------------------------------------------------
# Library Imports
# -----------------------------------------------------------------------------
from ..exceptions.validation import InvalidJsonError
from ..types import PWRCordType
from typing import Union

try:
    import json

    # If possible we should use this library since it is more performant than
    # the standard json library
    import orjson
except ModuleNotFoundError:
    # Just ignore it, but we should hurt performace by using the standard lib
    pass
else:
    # Tell that we can use orjson (successfuly imported)
    ORJSON_AVAILABLE = True

# -----------------------------------------------------------------------------
# Implementation
# -----------------------------------------------------------------------------
class JsonUtil:
    @staticmethod
    def validate(data: Union[str, bytes, bytearray, dict]) -> bool:
        if isinstance(data, dict):
            return True

        if ORJSON_AVAILABLE:
            try:
                orjson.loads(data)
            except (orjson.JSONDecodeError, TypeError):
                return False
            else:
                return True
        else:
            try:
                json.loads(data)
            except (json.JSONDecodeError, TypeError):
                return False
            else:
                return True

    @staticmethod
    def ensure_dict(
        json_deserializable: Union[str, bytes, bytearray, dict, PWRCordType]
    ) -> dict:
        # Let's check if the argument passed to this function is already a dict, so it must be returned as it was received
        if isinstance(json_deserializable, dict):
            return json_deserializable

        if isinstance(json_deserializable, PWRCordType):
            return json_deserializable.dict

        # According to the imported modules, we could use the best one if available falling back to the slowest if necessary
        if ORJSON_AVAILABLE:
            try:
                return orjson.loads(json_deserializable)

            except (orjson.JSONDecodeError, TypeError) as e:
                raise InvalidJsonError(e)
        else:
            try:
                return json.loads(json_deserializable)
            except (json.JSONDecodeError, TypeError) as e:
                raise InvalidJsonError(e)

    @staticmethod
    def ensure_bytes(json_serializable: Union[str, bytes, bytearray, dict]) -> bytes:
        # Let's check if the argument passed to this function is already bytes, so it must be returned as it was received
        if isinstance(json_serializable, bytes):
            if JsonUtil.validate(json_serializable):
                return json_serializable
            else:

                raise InvalidJsonError()

        if isinstance(json_serializable, str):
            if JsonUtil.validate(json_serializable):
                return json_serializable.encode("utf-8")
            else:

                raise InvalidJsonError()

        if isinstance(json_serializable, PWRCordType):
            json_serializable = json_serializable.dict

        if not isinstance(json_serializable, dict):
            # We don't want to convert an object that isn't a json
            raise InvalidJsonError(
                "Ensure that your json_serializable is a valid string, bytes, bytesarray or dict"
            )

        # According to the imported modules, we could use the best one if available falling back to the slowest if necessary
        if ORJSON_AVAILABLE:
            try:
                return orjson.dumps(json_serializable)

            except (orjson.JSONDecodeError, TypeError) as e:
                raise InvalidJsonError(e)
        else:
            try:
                return json.dumps(json_serializable).encode("utf-8")
            except (json.JSONDecodeError, TypeError) as e:
                raise InvalidJsonError(e)

    @classmethod
    def ensure_string(
        cls, json_serializable: Union[str, bytes, bytearray, dict]
    ) -> str:

        if isinstance(json_serializable, PWRCordType):
            json_serializable = json_serializable.dict
        # Let's check if the argument passed to this function is already bytes, so it must be returned as it was received
        if isinstance(json_serializable, str):
            if JsonUtil.validate(json_serializable):
                return json_serializable
            else:
                raise InvalidJsonError()

        if isinstance(json_serializable, bytes):
            if JsonUtil.validate(json_serializable):
                return json_serializable.decode("utf-8")
            else:
                raise InvalidJsonError()

        if not isinstance(json_serializable, dict):
            # We don't want to convert an object that isn't a json
            raise InvalidJsonError(
                "Ensure that your json_serializable is a valid string, bytes, bytesarray or dict"
            )

        # According to the imported modules, we could use the best one if available falling back to the slowest if necessary
        if ORJSON_AVAILABLE:
            try:
                return orjson.dumps(json_serializable).decode("utf-8")

            except (orjson.JSONDecodeError, TypeError) as e:
                raise InvalidJsonError(e)
        else:
            try:
                return json.dumps(json_serializable)

            except (json.JSONDecodeError, TypeError) as e:
                raise InvalidJsonError(e)


# -----------------------------------------------------------------------------
# Exports
# -----------------------------------------------------------------------------
__all__ = ["JsonUtil", "ORJSON_AVAILABLE"]
