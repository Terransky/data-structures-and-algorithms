from cc10 import Stack
from cc10 import Queue


def test_exists():
    assert Stack
    assert Queue

def test_push_one():
    stack = Stack()
    stack.push("apples")
    actual = stack.peek()
    expected = "apples"
    assert actual == expected

