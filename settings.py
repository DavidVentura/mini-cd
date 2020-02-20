from collections import namedtuple
from configparser import ConfigParser

Config = namedtuple('Config', 'repo_mappings working_dir_for_ansible')

_config = ConfigParser()
_config.read('config.ini')

config = Config(repo_mappings=dict(_config['repo_mappings']),
        working_dir_for_ansible=_config['main']['working_dir_for_ansible'])
