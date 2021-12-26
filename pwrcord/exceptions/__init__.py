# -*- coding: utf-8 -*-

"""PWRCord Exceptions
This submodule provides PWRCord related exceptions for easy debugging any error
found during the development of your project. All exceptions in our module pass
by our base PWRCordException which can be catched easely and includes useful 
information for fixing what's wrong with your code and focus on building your
projects 
"""

# -----------------------------------------------------------------------------
#                       PWRCord Base Exception
# -----------------------------------------------------------------------------
class PWRCordException(Exception):
    """
    Common base class for all PWRCord Exceptions
    """

    pass


# -----------------------------------------------------------------------------
# Module Level Imports
# -----------------------------------------------------------------------------
