"""SinglyLinkedList — 带哨兵节点的单链表。

使用 sentinel（哨兵）节点简化头部操作。
节点通过 next 引用串联，不使用连续内存。

支持头尾插入、头尾删除、按索引访问和转数组。
"""


class Node:
    """单链表节点。"""

    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next_node: "Node | None" = None) -> None:
        self.val: int = val
        self.next: Node | None = next_node


class SinglyLinkedList:
    """带哨兵节点的单链表（值类型为 int）。"""

    def __init__(self) -> None:
        self._sentinel: Node = Node()  # 哨兵节点，不存储有效数据
        self._size: int = 0

    def add_first(self, val: int) -> None:
        """在头部插入元素。O(1)。"""
        raise NotImplementedError("TODO: S02")

    def add_last(self, val: int) -> None:
        """在尾部插入元素。O(n)。"""
        raise NotImplementedError("TODO: S02")

    def remove_first(self) -> int:
        """删除并返回头部元素。空链表返回 -1。O(1)。"""
        raise NotImplementedError("TODO: S02")

    def remove_last(self) -> int:
        """删除并返回尾部元素。空链表返回 -1。O(n)。"""
        raise NotImplementedError("TODO: S02")

    def get(self, index: int) -> int:
        """按索引访问元素。越界返回 -1。O(n)。"""
        raise NotImplementedError("TODO: S02")

    def size(self) -> int:
        """返回当前元素个数。"""
        raise NotImplementedError("TODO: S02")

    def to_array(self) -> list[int]:
        """将链表元素按顺序转为数组。"""
        raise NotImplementedError("TODO: S02")
