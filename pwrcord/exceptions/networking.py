# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Library Level Imports
# -----------------------------------------------------------------------------
from typing import Dict

# -----------------------------------------------------------------------------
# Module Level Imports
# -----------------------------------------------------------------------------
from . import PWRCordException

# -----------------------------------------------------------------------------
#                     PWRCord Networking Base Exception
# -----------------------------------------------------------------------------
class PWRCordNetworkingException(PWRCordException):
    """
    Common base class for all PWRCord Networking Exceptions
    """

    pass


# -----------------------------------------------------------------------------
#                     PWRCord Networking Gateway Exceptions
# -----------------------------------------------------------------------------
class PWRCordGatewayException(PWRCordNetworkingException):
    """
    Common base class for all PWRCord Gateway Networking Exceptions
    """

    pass


class GatewayForceReconnect(PWRCordGatewayException):
    """
    All exceptions derivated from this are automatically reconnected to gateway
    """

    pass


class GatewayUnknownError(GatewayForceReconnect):
    """
    Something went wrong with gateway connection, try reconnecting? (4000)
    """

    pass


class GatewayUnknownOpcodeError(PWRCordGatewayException):
    """
    You sent an invalid Gateway opcode or an invalid payload for an opcode. Don't do that! (4001)
    """

    pass


class GatewayDecodeError(PWRCordGatewayException):
    """
    You sent an invalid payload to us. Don't do that! (4002)
    """

    pass


class GatewayNotAuthenticatedError(PWRCordGatewayException):
    """
    You sent us a payload prior to identifying. (4003)
    """

    pass


class GatewayAuthenticationFailedError(PWRCordGatewayException):
    """
    The account token sent with your identify payload is incorrect. (4004)
    """

    pass


class GatewayAlreadyAuthenticatedError(PWRCordGatewayException):
    """
    You sent more than one identify payload. Don't do that! (4005)
    """

    pass


class GatewayInvalidSeqError(GatewayForceReconnect):
    """
    The sequence sent when resuming the session was invalid. Reconnect and start a new session. (4007)
    """

    pass


class GatewayRateLimitedError(GatewayForceReconnect):
    """
    Rate limited (4008)
    """

    pass


class GatewaySessionTimedOutError(GatewayForceReconnect):
    """
    The sequence sent when resuming the session was invalid. Reconnect and start a new session. (4009)
    """

    pass


class GatewayInvalidShardError(PWRCordGatewayException):
    """
    You sent us an invalid shard when identifying. (4010)
    """

    pass


class GatewayShardingRequiredError(PWRCordGatewayException):
    """
    The session would have handled too many guilds - you are required to shard your connection in order to connect. (4010)
    """

    pass


class GatewayInvalidAPIVersionError(PWRCordGatewayException):
    """
    You sent an invalid version for the gateway.
    """

    pass


class GatewayInvalidIntentsError(PWRCordGatewayException):
    """
    You sent an invalid intent for a Gateway Intent. You may have incorrectly calculated the bitwise value.
    """

    pass


class GatewayDisallowedIntentsError(PWRCordGatewayException):
    """
    You sent a disallowed intent for a Gateway Intent. You may have tried to specify an intent that you have not enabled or are not approved for.
    """

    pass


GatewayError: Dict[int, PWRCordGatewayException] = {
    4000: GatewayUnknownError,
    4001: GatewayUnknownOpcodeError,
    4002: GatewayDecodeError,
    4003: GatewayNotAuthenticatedError,
    4004: GatewayAuthenticationFailedError,
    4005: GatewayAlreadyAuthenticatedError,
    4007: GatewayInvalidSeqError,
    4008: GatewayRateLimitedError,
    4009: GatewaySessionTimedOutError,
    4010: GatewayInvalidShardError,
    4011: GatewayShardingRequiredError,
    4012: GatewayInvalidAPIVersionError,
    4013: GatewayInvalidIntentsError,
    4014: GatewayDisallowedIntentsError,
}
"""Contains the error codes as keys and the exceptions as values"""

# -----------------------------------------------------------------------------
#                     PWRCord Networking HTTP Exceptions
# -----------------------------------------------------------------------------
class PWRCordHTTPException(PWRCordNetworkingException):
    """
    Common base class for all PWRCord HTTP Networking Exceptions
    """

    pass


class HTTPClientError(PWRCordHTTPException):
    """
    Represents a failure on data sent by client to discord servers (4xx errors)
    """

    pass


class HTTPBadRequestError(HTTPClientError):
    """
    The request was improperly formatted, or the server couldn't understand it (400).
    """

    pass


class HTTPUnauthorizedError(HTTPClientError):
    """
    The Authorization header was missing or invalid (401).
    """

    pass


class HTTPForbiddenError(HTTPClientError):
    """
    The Authorization token you passed did not have permission to the resource (403).
    """

    pass


class HTTPNotFoundError(HTTPClientError):
    """
    The resource at the location specified doesn't exist (404).
    """

    pass


class HTTPMethodNotAllowedError(HTTPClientError):
    """
    The HTTP method used is not valid for the location specified (405).
    """

    pass


class HTTPTooManyRequestsError(HTTPClientError):
    """
    You are being rate limited (429).
    """

    pass


class HTTPServerError(PWRCordHTTPException):
    """
    Represents a failure on discord servers (5xx errors)
    """

    pass


class HTTPGatewayUnavailableError(HTTPServerError):
    """
    There was not a gateway available to process your request. Wait a bit and retry (502).
    """

    pass


HTTPError: Dict[int, PWRCordHTTPException] = {
    400: HTTPBadRequestError,
    401: HTTPUnauthorizedError,
    403: HTTPForbiddenError,
    404: HTTPNotFoundError,
    405: HTTPMethodNotAllowedError,
    429: HTTPTooManyRequestsError,
    502: HTTPGatewayUnavailableError,
}
"""Contains the error codes as keys and the exceptions as values"""

# -----------------------------------------------------------------------------
#                     PWRCord Networking RPC Exceptions
# -----------------------------------------------------------------------------
class PWRCordRPCException(PWRCordNetworkingException):
    """
    Common base class for all PWRCord RPC Networking Exceptions
    """

    pass


class RPCInvalidClientIDError(PWRCordRPCException):
    """
    You connected to the RPC server with an invalid client ID. (4000)
    """


class RPCInvalidOriginError(PWRCordRPCException):
    """
    You connected to the RPC server with an invalid origin. (4001)
    """


class RPCRateLimitedError(PWRCordRPCException):
    """
    Rate Limited. (4002)
    """


class RPCTokenRevokedError(PWRCordRPCException):
    """
    The OAuth2 token associated with a connection was revoked, get a new one! (4003)
    """


class RPCInvalidVersionError(PWRCordRPCException):
    """
    The RPC Server version specified in the connection string was not valid. (4004)
    """


class RPCInvalidEncodingError(PWRCordRPCException):
    """
    The encoding specified in the connection string was not valid. (4005)
    """


RPCError: Dict[int, PWRCordRPCException] = {
    4000: RPCInvalidClientIDError,
    4001: RPCInvalidOriginError,
    4002: RPCRateLimitedError,
    4003: RPCTokenRevokedError,
    4004: RPCInvalidVersionError,
    4005: RPCInvalidEncodingError,
}
"""Contains the error codes as keys and the exceptions as values"""
