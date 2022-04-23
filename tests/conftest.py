from src.Node import Node
import pytest


@pytest.fixture()
def empty_node():
    return Node()

