from src.core.Node import Node
from src.core.LinkedList import LinkedList
import pytest


@pytest.fixture()
def empty_node():
    return Node()


@pytest.fixture()
def list_with_random_data():
    data = [1, 2, 3, 4, 5]
    return LinkedList(data)
