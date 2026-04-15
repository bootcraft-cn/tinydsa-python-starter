"""DoublyLinkedList — 带双向哨兵的双向链表 Deque。

使用 sentinel head + sentinel tail 双哨兵模式，
每个节点持有 prev 和 next 两个引用，实现两端 O(1) 操作。
"""


class DLLNode:
    """双向链表节点。"""

    __slots__ = ("val", "prev", "next")

    def __init__(
        self,
        val: int = 0,
        prev: "DLLNode | None" = None,
        next_node: "DLLNode | None" = None,
    ) -> None:
        self.val: int = val
        self.prev: DLLNode | None = prev
        self.next: DLLNode | None = next_node


class DoublyLinkedList:
    """带双向哨兵的双向链表（值类型为 int）。"""

    def __init__(self) -> None:
        self._head: DLLNode = DLLNode()  # 头哨兵
        self._tail: DLLNode = DLLNode()  # 尾哨兵
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size: int = 0

    def add_first(self, val: int) -> None:
        """在头部插入元素。O(1)。"""
        raise NotImplementedError("TODO: S03")

    def add_last(self, val: int) -> None:
        """在尾部插入元素。O(1)。"""
        raise NotImplementedError("TODO: S03")

    def remove_first(self) -> int:
        """删除并返回头部元素。空链表返回 -1。O(1)。"""
        raise NotImplementedError("TODO: S03")

    def remove_last(self) -> int:
        """删除并返回尾部元素。空链表返回 -1。O(1)。"""
        raise NotImplementedError("TODO: S03")

    def get(self, index: int) -> int:
        """按索引访问元素。越界返回 -1。O(n)。"""
        raise NotImplementedError("TODO: S03")

    def size(self) -> int:
        """返回当前元素个数。"""
        raise NotImplementedError("TODO: S03")

    def to_array(self) -> list[int]:
        """将链表元素按正序转为数组。"""
        raise NotImplementedError("TODO: S03")

    def to_array_reverse(self) -> list[int]:
        """将链表元素按反序转为数组（验证 prev 链正确性）。"""
        raise NotImplementedError("TODO: S03")
