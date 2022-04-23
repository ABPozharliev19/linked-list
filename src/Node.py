from typing import Any, TypeVar, Union, Optional

N = TypeVar('N', bound='Node')


class Node:
    _data = None
    _prev = None
    _next = None

    def __init__(self: N, data: Any = None, prev_node: Union[N, None] = None, next_node: Union[N, None] = None) -> None:
        self._data = data
        self._prev = prev_node
        self._next = next_node

    def __repr__(self: N) -> str:
        return f"Node object with data: {self._data}, " \
               f"prev: {f'Node({self._prev.data})' if self._prev else None}, " \
               f"next: {f'Node({self._next.data})' if self._next else None}"

    @property
    def data(self: N) -> Any:
        return self._data

    @data.setter
    def data(self: N, data: Any) -> None:
        self._data = data

    @property
    def prev(self: N) -> Union[N, None]:
        return self._prev

    @prev.setter
    def prev(self: N, prev_node: Union[N, None]) -> None:
        self._prev = prev_node

    @property
    def next(self: N) -> Union[N, None]:
        return self._next

    @next.setter
    def next(self: N, next_node: Union[N, None]) -> None:
        self._next = next_node
