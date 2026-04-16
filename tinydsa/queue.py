"""Queue — 基于 ArrayDeque 的队列实现（FIFO）。

将 ArrayDeque 作为底层，通过委托调用实现队列语义。
enqueue 在尾端，dequeue/front 在头端。
"""

from tinydsa.array_deque import ArrayDeque


class Queue:
    """基于 ArrayDeque 的队列（值类型为 int）。"""

    def __init__(self) -> None:
        self._deque = ArrayDeque()

    def enqueue(self, val: int) -> None:
        """将元素加入队尾。"""
        raise NotImplementedError("TODO: S05")

    def dequeue(self) -> int:
        """取出并返回队首元素。空队列返回 -1。"""
        raise NotImplementedError("TODO: S05")

    def front(self) -> int:
        """查看队首元素但不取出。空队列返回 -1。"""
        raise NotImplementedError("TODO: S05")

    def queue_size(self) -> int:
        """返回队列中元素个数。"""
        raise NotImplementedError("TODO: S05")
