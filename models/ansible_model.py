from __future__ import print_function

from utils.ansible_model import AnsbileModel

import sys

sys.path.append('.')


class Ping(AnsbileModel):
    def __init__(self):
        super(Ping, self).__init__(None)
        self.ansible_module_name = 'ping'


class Shell(AnsbileModel):
    def __init__(self, args):
        super(Shell, self).__init__(args)
        self.ansible_module_name = 'shell'


class Juniper(AnsbileModel):
    def __init__(self):
        super(Juniper, self).__init__(None)

    def commands(self, args, display='text'):
        self.ansible_module_name = 'junos_command'
        self.action_dict['commands'] = args
        self.action_dict['display'] = display


class Cisco(AnsbileModel):
    def __init__(self):
        super(Cisco, self).__init__(None)

    def commands(self, args):
        self.ansible_module_name = 'ios_command'
        self.action_dict['commands'] = args

    def config(self, src):
        self.ansible_module_name = 'ios_config'
        self.action_dict['src'] = src
        self.action_dict['save_when'] = 'modified'
