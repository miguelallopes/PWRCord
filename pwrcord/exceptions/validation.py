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
#                     PWRCord Validation Base Exception
# -----------------------------------------------------------------------------
class PWRCordValidationException(PWRCordException):
    """
    Common base class for all PWRCord data validation Exceptions
    """

    pass


# -----------------------------------------------------------------------------
#                     PWRCord Json Validation Exception
# -----------------------------------------------------------------------------
class InvalidJsonError(PWRCordValidationException):
    """
    Raised when specified JSON is not valid
    """
