#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: BSD
#   https://raw.githubusercontent.com/stonier/groot_rocker_extensions/devel/LICENSE
#

##############################################################################
# Imports
##############################################################################

from . import utilities

##############################################################################
# Tests
##############################################################################


class ExtensionTest(utilities.ExtensionTestCase):

    def setUp(self):
        self.extension_name = "named_prompt"
        super().setUp()
