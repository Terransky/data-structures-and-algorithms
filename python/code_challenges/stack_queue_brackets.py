from python.data_structures.queue import Queue
from python.stacks_and_queues.cc10 import *


def multi_bracket_validation(string):
    """input: string, do the brackets match, output: boolean"""

    if string is "[]":
        return True

    elif string is "][":
        return False
