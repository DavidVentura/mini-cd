from collections import namedtuple
from configparser import ConfigParser

Config = namedtuple('Config', 'working_dir_for_ansible')

_config = ConfigParser()
_config.read('config.ini')

config = Config(working_dir_for_ansible=_config['main']['working_dir_for_ansible'])
