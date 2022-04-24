def test_list_getitem(list_with_random_data):
    assert list_with_random_data[0] == 1
    assert list_with_random_data[1] == 2
    assert list_with_random_data[2] == 3
    assert list_with_random_data[3] == 4
    assert list_with_random_data[4] == 5


def test_list_length(list_with_random_data):
    assert len(list_with_random_data) == 5
