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

from rocker.extensions import RockerExtension

##############################################################################
# Extension
##############################################################################


class Name(RockerExtension):

    name = "groot_name"

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
        return ''

    def get_docker_args(self, cli_args):
        args = ''
        name = cli_args.get('name', None)
        if name:
            args += f" --name {name} "
        return args

    @staticmethod
    def register_arguments(parser, defaults={}):
        parser.add_argument(
            '--groot-name',
            default='',
            help='Name of the container, also sets ROCKER_NAME.'
        )


class NamedPrompt(RockerExtension):

    name = 'groot_named_prompt'

    @classmethod
    def get_name(cls):
        return cls.name

    def get_environment_subs(self):
        user_vars = ['name', 'uid', 'gid', 'gecos', 'dir', 'shell']
        userinfo = pwd.getpwuid(os.getuid())
        environment_substitutions = {
            k: getattr(userinfo, 'pw_' + k)
            for k in user_vars
        }
        return environment_substitutions

    def precondition_environment(self, cli_args):
        pass

    def validate_environment(self, cli_args):
        pass

    def get_preamble(self, cli_args):
        return ''

    def get_snippet(self, cli_args):
        snippet = pkgutil.get_data(
            'groot_rocker',
            'templates/named_prompt.Dockerfile.em'
        ).decode('utf-8')
        substitutions = self.get_environment_subs()
        print(f"Substitutions: {substitutions}")
        dockerfile = em.expand(snippet, substitutions)
        print(f"Dockerfile: {dockerfile}")
        return dockerfile

    def get_docker_args(self, cli_args):
        return ""

    @staticmethod
    def register_arguments(parser):
        parser.add_argument(
            '--groot-named-prompt',
            action='store_true',
            help='export a named prompt via PS1 to ~/.bash_profile'
        )
