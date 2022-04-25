def test_empty_node_data(node_empty):
    assert node_empty.data is None


def test_empty_node_prev(node_empty):
    assert node_empty.prev is None


def test_empty_node_next(node_empty):
    assert node_empty.next is None
