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


def test_list_clear(list_with_random_data):
    list_with_random_data.clear()
    with pytest.raises(IndexError):
        list_with_random_data[0] = 1


def test_list_count1(list_with_random_data):
    counter: int = list_with_random_data.count(1)
    assert counter == 1


def test_list_count2(list_with_random_data):
    for i in range(len(list_with_random_data)):
        list_with_random_data[i] = 1
    counter: int = list_with_random_data.count(1)

    assert counter == len(list_with_random_data)


def test_empty_list_count1(list_empty):
    count: int = list_empty.count(1)
    assert count == 0


def test_empty_list_count2(list_empty):
    for _ in range(10):
        list_empty.append(1)

    count: int = list_empty.count(1)
    assert count == len(list_empty)


def test_list_extend(list_with_random_data):
    temp_list = [1, 2, 3]
    list_with_random_data.extend(temp_list)
    assert list_with_random_data[0] == 1
    assert list_with_random_data[1] == 2
    assert list_with_random_data[2] == 3
    assert list_with_random_data[3] == 4
    assert list_with_random_data[4] == 5
    assert list_with_random_data[5] == 1
    assert list_with_random_data[6] == 2
    assert list_with_random_data[7] == 3


def test_empty_list_extend(list_empty):
    temp_list = [1, 2, 3]
    list_empty.extend(temp_list)
    assert list_empty[0] == 1
    assert list_empty[1] == 2
    assert list_empty[2] == 3


def test_empty_list_insert(list_empty):
    with pytest.raises(IndexError):
        list_empty.insert(0, 0)


def test_list_insert1(list_with_random_data):
    for _ in range(6):
        list_with_random_data.insert(-1, 1)
    assert list_with_random_data[0] == 1
    assert list_with_random_data[1] == 1
    assert list_with_random_data[2] == 1
    assert list_with_random_data[3] == 1
    assert list_with_random_data[4] == 1
    assert list_with_random_data[6] == 1
    assert list_with_random_data[7] == 2
    assert list_with_random_data[8] == 3
    assert list_with_random_data[9] == 4
    assert list_with_random_data[10] == 5


def test_list_insert2(list_with_random_data):
    for _ in range(6):
        list_with_random_data.insert(0, 2)
    assert list_with_random_data[0] == 1
    assert list_with_random_data[1] == 2
    assert list_with_random_data[2] == 2
    assert list_with_random_data[3] == 2
    assert list_with_random_data[4] == 2
    assert list_with_random_data[6] == 2
    assert list_with_random_data[7] == 2
    assert list_with_random_data[8] == 3
    assert list_with_random_data[9] == 4
    assert list_with_random_data[10] == 5
