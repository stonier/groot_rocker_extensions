#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: BSD
#   https://raw.githubusercontent.com/stonier/groot_rocker_extensions/devel/LICENSE
#

##############################################################################
# Imports
##############################################################################

import getpass
import os
import pathlib
import pwd

from . import utilities

##############################################################################
# Tests
##############################################################################


class UserExtensionTest(utilities.ExtensionTestCase):

    def setUp(self):
        self.extension_name = "named_prompt"
        super().setUp()
