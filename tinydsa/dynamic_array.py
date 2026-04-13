"""DynamicArray — 手动扩容动态数组。

底层使用固定长度的 Python list（[None] * capacity）模拟原生数组。
禁止使用 list.append()、list.insert()、list.pop() 等内置动态方法。

初始容量 8，满时扩容为 2 倍，使用率低于 25% 时缩容为 1/2（最小容量 8）。
"""

_DEFAULT_CAPACITY = 8


class DynamicArray:
    """可自动扩容和缩容的动态数组（值类型为 int）。"""

    def __init__(self) -> None:
        self._capacity: int = _DEFAULT_CAPACITY
        self._size: int = 0
        self._data: list = [None] * self._capacity

    def add(self, val: int) -> None:
        """在末尾追加元素。若数组已满，先扩容再追加。"""
        raise NotImplementedError("TODO: S01")

    def get(self, index: int) -> int:
        """按索引访问元素。越界返回 -1。"""
        raise NotImplementedError("TODO: S01")

    def set(self, index: int, val: int) -> None:
        """按索引修改元素。越界不做任何操作。"""
        raise NotImplementedError("TODO: S01")

    def remove_at(self, index: int) -> int:
        """按索引删除元素并返回被删除的值。

        删除后右侧元素左移一位。越界返回 -1。
        若删除后 size < capacity / 4，缩容为 capacity / 2（最小 8）。
        """
        raise NotImplementedError("TODO: S01")

    def size(self) -> int:
        """返回当前元素个数。"""
        raise NotImplementedError("TODO: S01")

    def capacity(self) -> int:
        """返回当前底层数组的容量。"""
        raise NotImplementedError("TODO: S01")

    # ------------------------------------------------------------------
    # 内部方法（提示：你可能需要实现以下辅助方法）
    # ------------------------------------------------------------------

    def _resize(self, new_capacity: int) -> None:
        """将底层数组扩容/缩容到 new_capacity。

        分配新数组，复制已有元素，替换旧数组。
        """
        raise NotImplementedError("TODO: S01")
