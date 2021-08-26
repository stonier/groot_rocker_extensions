#!/usr/bin/env python
#
# License: BSD
#   https://raw.githubusercontent.com/stonier/groot_rocker_extensions/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Forward PulseAudio configuration into the container. Only tested in Ubuntu 18.
"""

##############################################################################
# Imports
##############################################################################

import os
import re
import typing

import groot_rocker

##############################################################################
# Extension
##############################################################################


class PulseAudio(groot_rocker.extensions.RockerExtension):
    """
    Forward PulseAudio configuration into the container. This will not work without --user.
    """
    @classmethod
    def get_name(cls) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()  # CamelCase to underscores

    def precondition_environment(self, unused_cli_args: typing.Dict[str, str]):
        pass

    def validate_environment(self, unused_cli_args: typing.Dict[str, str]):
        pass

    def get_preamble(self, unused_cli_args: typing.Dict[str, str]) -> str:
        return ''

    def get_snippet(self, unused_cli_args: typing.Dict[str, str]) -> str:
        return ''

    def get_docker_args(self, cli_args: typing.Dict[str, str]) -> str:
        args = ''
        # Ensure paths exist and add them to the run.
        for source_path, target_path in [
            ["/usr/share/alsa", "/usr/share/alsa"],
            [os.path.expanduser('~/.config/pulse'), "/.config/pulse"],
            [f"/run/user/{os.getuid()}/pulse/native", f"/run/user/{os.getuid()}/pulse/native"]
        ]:
            assert os.path.exists(source_path), f"Path {source_path} does not exist. You PulseAudio configuration differs."
            args += f" -v {source_path}:{target_path}"
        args += f' --env "PULSE_SERVER=unix:/run/user/{os.getuid()}/pulse/native"'
        return args

    @staticmethod
    def register_arguments(parser, defaults={}):
        parser.add_argument(
            '--pulse_audio',
            action='store_true',
            default=defaults.get('pulseaudio', None),
            help="Forward PulseAudio into the container"
        )
