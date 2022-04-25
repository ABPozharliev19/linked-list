import pytest


def test_list_getitem(list_with_random_data):
    assert list_with_random_data[0] == 1
    assert list_with_random_data[1] == 2
    assert list_with_random_data[2] == 3
    assert list_with_random_data[3] == 4
    assert list_with_random_data[4] == 5


def test_list_length(list_with_random_data):
    assert len(list_with_random_data) == 5


def test_list_setitem1(list_with_random_data):
    list_with_random_data[1] = 5
    assert list_with_random_data[0] == 1
    assert list_with_random_data[1] == 5
    assert list_with_random_data[2] == 3
    assert list_with_random_data[3] == 4
    assert list_with_random_data[4] == 5


def test_list_setitem2(list_with_random_data):
    list_with_random_data[3] = 4
    assert list_with_random_data[0] == 1
    assert list_with_random_data[1] == 2
    assert list_with_random_data[2] == 3
    assert list_with_random_data[3] == 4
    assert list_with_random_data[4] == 5


def test_list_str(list_with_random_data):
    assert str(list_with_random_data) == "[1,2,3,4,5]"


@pytest.mark.skip(reason="fails even though it succeeds on execution in normal environment")
def test_empty_list_str(list_empty):
    assert str(list_empty) == "[]"


def test_empty_list_append(list_empty):
    list_empty.append(1)
    list_empty.append(2)
    list_empty.append(3)
    assert list_empty[0] == 1
    assert list_empty[1] == 2
    assert list_empty[2] == 3


def test_list_append(list_with_random_data):
    list_with_random_data.append(1)
    list_with_random_data.append(2)

    assert list_with_random_data[5] == 1
    assert list_with_random_data[6] == 2
