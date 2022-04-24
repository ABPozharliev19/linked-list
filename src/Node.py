from typing import Any, TypeVar, Union, Optional
import copy

class Node:
    def __init__(self, data: Any = None, prev_node: Union['Node', None] = None, next_node: Union['Node', None] = None) -> None:
        self._data: Any = data
        self._prev: Optional[Node] = prev_node
        self._next: Optional[Node] = next_node

    def __str__(self) -> str:
        return str(self._data)

    def __repr__(self) -> str:
        return f"Node object with data: {self._data}, " \
               f"prev: {f'Node({self._prev.data})' if self._prev else None}, " \
               f"next: {f'Node({self._next.data})' if self._next else None}"

    def copy(self) -> 'Node':
        return copy.copy(self)

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, data: Any) -> None:
        self._data = data

    @property
    def prev(self) -> Union['Node', None]:
        return self._prev

    @prev.setter
    def prev(self, prev_node: Union['Node', None]) -> None:
        self._prev = prev_node

    @property
    def next(self) -> Union['Node', None]:
        return self._next

    @next.setter
    def next(self, next_node: Union['Node', None]) -> None:
        self._next = next_node
