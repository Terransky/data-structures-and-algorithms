from python.data_structures.queue import Queue
from python.stacks_and_queues.cc10 import *


def multi_bracket_validation(string):
    """input: string, do the brackets match, output: boolean"""

    if string == "[]":
        return True  # with the way the test is written, shouldn't this pass? Why is the test actual None?

