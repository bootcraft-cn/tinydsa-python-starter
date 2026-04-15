"""ArrayDeque — 基于环形缓冲区的双端队列。

使用 head/tail 指针在固定数组上实现两端 O(1) 插入和删除，
满时翻倍扩容。通过取模运算实现首尾环绕。
"""


class ArrayDeque:
    """基于环形缓冲区的双端队列（值类型为 int）。"""

    _DEFAULT_CAPACITY = 8

    def __init__(self) -> None:
        self._data: list[int | None] = [None] * ArrayDeque._DEFAULT_CAPACITY
        self._head: int = 0
        self._tail: int = 0
        self._size: int = 0

    def add_first(self, val: int) -> None:
        """在头部插入元素。均摊 O(1)。"""
        raise NotImplementedError("TODO: S04")

    def add_last(self, val: int) -> None:
        """在尾部插入元素。均摊 O(1)。"""
        raise NotImplementedError("TODO: S04")

    def remove_first(self) -> int:
        """删除并返回头部元素。空队列返回 -1。O(1)。"""
        raise NotImplementedError("TODO: S04")

    def remove_last(self) -> int:
        """删除并返回尾部元素。空队列返回 -1。O(1)。"""
        raise NotImplementedError("TODO: S04")

    def get(self, index: int) -> int:
        """按逻辑索引访问元素。越界返回 -1。O(1)。"""
        raise NotImplementedError("TODO: S04")

    def size(self) -> int:
        """返回当前元素个数。"""
        raise NotImplementedError("TODO: S04")

    def to_array(self) -> list[int]:
        """将队列元素按逻辑顺序转为数组。"""
        raise NotImplementedError("TODO: S04")
