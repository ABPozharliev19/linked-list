from Node import Node
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

    def __str__(self) -> str:
        if self._head.data is not None:
            str_to_return = "["
            temp_node: Node = self._head
            for _ in range(self._len - 1):
                str_to_return = str_to_return + str(temp_node.data) + ","
                temp_node = temp_node.next

            str_to_return = str_to_return + str(temp_node.data) + "]"

            return str_to_return

        else:
            return "[]"

    def __getitem__(self, index: int) -> Any:
        self._check_if_index_is_integer(index)
        self._check_if_index_is_in_bound(index)

        temp_node: Node = self._head.copy()

        temp_node = self._traverse_list(index, temp_node)

        return temp_node.data

    def __setitem__(self, index: int, value: Any) -> None:
        self._check_if_index_is_integer(index)
        self._check_if_index_is_in_bound(index)

        temp_node: Node = self._head

        temp_node = self._traverse_list(index, temp_node)

        temp_node.data = value

    def append(self, element: Any) -> None:
        if not self._is_head_initialized:
            self._head.data = element
            self._is_head_initialized = True
        else:
            new_node: Node = Node(element, self._tail)
            self._tail.next = new_node
            self._tail = new_node
        self._len = self._len + 1

    def clear(self) -> None:
        self._head = Node()
        self._tail = self._head
        self._is_head_initialized = False
        self._len = 0

    def count(self, value: Any) -> int:
        temp_node: Node = self._head

        counter: int = 0

        for _ in range(self._len):
            if temp_node.data == value:
                counter = counter + 1
            if temp_node.next:
                temp_node = temp_node.next

        return counter

    def extend(self, contents: Iterable[Any]) -> None:
        for item in contents:
            self.append(item)

    def insert(self, index: int, element: Any) -> None:
        self._check_if_index_is_integer(index)

        if self._len > 0:
            if index == -1:
                new_node = Node(element)
                new_node.next = self._head
                self._head.prev = new_node
                self._head = new_node

            elif index == self._len - 1:
                new_node = Node(element, self._tail)
                self._tail.next = new_node
                self._tail = new_node

            else:
                temp_node: Node = self._head
                temp_node = self._traverse_list(index, temp_node)
                new_node = Node(element, temp_node, temp_node.next)
                temp_node.next.prev = new_node
                temp_node.next = new_node

            self._len = self._len + 1
        else:
            if index < 0 or index >= self._len:
                raise IndexError("index out of bound")
            else:
                raise ValueError("list is empty, cannot insert into an empty list")

    def remove(self, value: Any) -> bool:
        temp_node: Node = self._head

        has_deleted_anything: bool = False

        for index in range(self._len + 1):
            if temp_node.data == value:
                if index == 0:
                    if self._len == 0:
                        self._head.data = 0
                        self._len = 0

                        self._is_head_initialized = False

                        has_deleted_anything = True

                        break

                    else:
                        self._head.next.prev = None
                        self._head = self._head.next

                        self._len = self._len - 1

                        has_deleted_anything = True

                        break

                elif index == self._len - 1:
                    if self._len == 1:
                        self._head.data = None
                        self._len = 0

                        self._is_head_initialized = False

                        has_deleted_anything = True

                        break

                    else:
                        self._tail = self._tail.prev
                        self._tail.next = None

                        self._len = self._len - 1

                        has_deleted_anything = True

                        break

                elif value == temp_node.data:
                    temp_node.prev.next = temp_node.next
                    temp_node.next.prev = temp_node.prev

                    self._len = self._len - 1

                    as_deleted_anything = True

                    break

            if temp_node.next is not None:
                temp_node = temp_node.next

        return has_deleted_anything

    def _check_if_index_is_in_bound(self, index: int) -> None:
        if index >= self._len:
            raise IndexError(f"{index} index out of range")

    @staticmethod
    def _check_if_index_is_integer(index: int) -> None:
        if not isinstance(index, int):
            raise TypeError(f"'{type(index)}' not supported for indexation")

    @staticmethod
    def _traverse_list(index: int, temp_node: Node) -> Node:
        for _ in range(index):
            if temp_node.next:
                temp_node = temp_node.next
        return temp_node
