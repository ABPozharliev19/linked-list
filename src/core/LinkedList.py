from src.core.Node import Node
from typing import Iterable, Optional, Any


class LinkedList:
    _head: Node = Node()
    _tail: Node = _head

    _len: int = 0

    _is_head_initialized: bool = False

    def __init__(self, args: Optional[Iterable[Any]] = None) -> None:
        if args is not None:
            try:
                _ = iter(args)
            except TypeError:
                raise TypeError(f"'{type(args)}' not supported for constructor. \n"
                                f"Call with iterable instead.")

            for item in args:
                if not self._is_head_initialized:
                    self._head.data = item
                    self._is_head_initialized = True
                    self._len = self._len + 1

                else:
                    new_node: Node = Node(item, self._tail)

                    self._tail.next = new_node
                    self._tail = new_node

                    self._len = self._len + 1

    def __len__(self) -> int:
        return self._len

    def __getitem__(self, index: int) -> Any:
        self._check_if_index_is_in_bound(index)
        self._check_if_index_is_integer(index)

        temp_node: Node = self._head

        self._traverse_list(index, temp_node)

        return temp_node.data

    def __setitem__(self, index: int, value: Any) -> None:
        self._check_if_index_is_in_bound(index)
        self._check_if_index_is_integer(index)

        temp_node: Node = self._head

        self._traverse_list(index, temp_node)

        temp_node.data = value

    def _check_if_index_is_in_bound(self, index: int) -> None:
        if index >= self._len:
            raise IndexError(f"{index} index out of range")

    @staticmethod
    def _check_if_index_is_integer(index: int):
        if not isinstance(index, int):
            raise TypeError(f"'{type(index)}' not supported for indexation")

    @staticmethod
    def _traverse_list(index: int, temp_node: Node):
        for _ in range(index):
            if temp_node.next:
                temp_node = temp_node.next


if __name__ == "__main__":
    konche = [1,2, 3]
    gosho = LinkedList(konche)
    gosho[1] = 5
    print(gosho[1])
    print(1)