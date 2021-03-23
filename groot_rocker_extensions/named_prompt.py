#!/usr/bin/env python
#
# License: BSD
#   https://raw.githubusercontent.com/stonier/groot_rocker/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Export a coloured, named prompt to ~/.bash_profile on container creation.
"""

##############################################################################
# Imports
##############################################################################

import em
import pkgutil
import os
import pwd

import groot_rocker

##############################################################################
# Extension
##############################################################################


class NamedPrompt(groot_rocker.extensions.RockerExtension):

    name = 'named_prompt'

    @classmethod
    def get_name(cls):
        return cls.name

    def precondition_environment(self, cli_args):
        pass

    def validate_environment(self, cli_args):
        pass

    def get_preamble(self, cli_args):
        return ''

    def get_snippet(self, cli_args):
        snippet = pkgutil.get_data(
            'groot_rocker_extensions',
            'templates/named_prompt.Dockerfile.em'
        ).decode('utf-8')
        substitutions = {}
        userinfo = pwd.getpwuid(os.getuid())
        substitutions['user_name'] = getattr(userinfo, 'pw_' + 'name')
        if 'name' in cli_args and cli_args['name']:
            substitutions['container_name'] = cli_args['name']
        else:
            substitutions['container_name'] = r'\h'
        dockerfile = em.expand(snippet, substitutions)
        return dockerfile

    def get_docker_args(self, cli_args):
        return ""

    @staticmethod
    def register_arguments(parser, defaults={}):
        # TODO: what to do with the defaults arg?
        parser.add_argument(
            '--named-prompt',
            action='store_true',
            help='export a named prompt via PS1 to ~/.bash_profile'
        )
