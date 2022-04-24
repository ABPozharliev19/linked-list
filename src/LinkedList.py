from Node import Node
from typing import Iterable, Optional, Any, Type


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
                                f"Call with Iterator instead.")

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
        if not isinstance(index, int):
            raise TypeError(f"'{type(index)}' not supported for indexation")

        if index >= self._len:
            raise IndexError(f"{index} index out of range")

        new_head: Node = self._head.copy()
        for _ in range(index):
            new_head = new_head.next

        return new_head.data


if __name__ == "__main__":
    konche = [1, 2, 3]
    gosho = LinkedList(konche)
    print(len(gosho))
    print(gosho[2])
    print(1)