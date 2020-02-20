from enum import Enum, auto
from collections import namedtuple

class Result(Enum):
    Success = auto()
    Failure = auto()

Response = namedtuple('Response', 'result message')

