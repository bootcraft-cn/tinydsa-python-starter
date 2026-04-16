"""Stack — 基于 ArrayDeque 的栈实现（LIFO）。

将 ArrayDeque 作为底层，通过委托调用实现栈语义。
push/pop/peek 操作均基于 Deque 尾端。
"""

from tinydsa.array_deque import ArrayDeque


class Stack:
    """基于 ArrayDeque 的栈（值类型为 int）。"""

    def __init__(self) -> None:
        self._deque = ArrayDeque()

    def push(self, val: int) -> None:
        """将元素压入栈顶。"""
        raise NotImplementedError("TODO: S05")

    def pop(self) -> int:
        """弹出并返回栈顶元素。空栈返回 -1。"""
        raise NotImplementedError("TODO: S05")

    def peek(self) -> int:
        """查看栈顶元素但不弹出。空栈返回 -1。"""
        raise NotImplementedError("TODO: S05")

    def stack_size(self) -> int:
        """返回栈中元素个数。"""
        raise NotImplementedError("TODO: S05")
