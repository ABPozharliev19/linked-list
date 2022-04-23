import pytest
from tests.conftest import empty_node


def test_empty_node_data(empty_node):
    assert empty_node.data is None

def test_empty_node_prev(empty_node):
    assert empty_node.prev is None

def test_empty_node_next(empty_node):
    assert empty_node.next is None
