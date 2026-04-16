"""test_s05.py — S05 Stack & Queue test driver.

Provided by tinydsa-starter. Do NOT modify.
The tester runs this file to verify your Stack and Queue implementation.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from tinydsa import Stack, Queue


def emit(test_name: str, result: str) -> None:
    print(f"TEST:{test_name}")
    print(f"RESULT:{result}")


def main() -> None:
    # ===== Stack Tests =====

    # --- 基本操作 ---
    s = Stack()
    emit("stack_initial_size", str(s.stack_size()))  # 0

    # --- push + pop (LIFO) ---
    s.push(1)
    s.push(2)
    s.push(3)
    emit("stack_pop_1", str(s.pop()))  # 3
    emit("stack_pop_2", str(s.pop()))  # 2
    emit("stack_pop_3", str(s.pop()))  # 1

    # --- 空栈 pop ---
    emit("stack_pop_empty", str(s.pop()))  # -1

    # --- peek ---
    s2 = Stack()
    s2.push(10)
    s2.push(20)
    emit("stack_peek", str(s2.peek()))  # 20
    emit("stack_size_after_peek", str(s2.stack_size()))  # 2 (peek 不改变 size)

    # --- 空栈 peek ---
    s3 = Stack()
    emit("stack_peek_empty", str(s3.peek()))  # -1

    # --- push + pop + size ---
    s4 = Stack()
    s4.push(10)
    s4.push(20)
    s4.push(30)
    emit("stack_size_3", str(s4.stack_size()))  # 3
    s4.pop()
    emit("stack_size_after_pop", str(s4.stack_size()))  # 2

    # --- 多次 push/pop 交替 ---
    s5 = Stack()
    s5.push(1)
    s5.push(2)
    emit("stack_alternate_pop_1", str(s5.pop()))  # 2
    s5.push(3)
    emit("stack_alternate_peek", str(s5.peek()))  # 3
    emit("stack_alternate_pop_2", str(s5.pop()))  # 3
    emit("stack_alternate_pop_3", str(s5.pop()))  # 1
    emit("stack_alternate_size", str(s5.stack_size()))  # 0

    # ===== Queue Tests =====

    # --- 基本操作 ---
    q = Queue()
    emit("queue_initial_size", str(q.queue_size()))  # 0

    # --- enqueue + dequeue (FIFO) ---
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    emit("queue_dequeue_1", str(q.dequeue()))  # 1
    emit("queue_dequeue_2", str(q.dequeue()))  # 2
    emit("queue_dequeue_3", str(q.dequeue()))  # 3

    # --- 空队列 dequeue ---
    emit("queue_dequeue_empty", str(q.dequeue()))  # -1

    # --- front ---
    q2 = Queue()
    q2.enqueue(10)
    q2.enqueue(20)
    emit("queue_front", str(q2.front()))  # 10
    emit("queue_size_after_front", str(q2.queue_size()))  # 2 (front 不改变 size)

    # --- 空队列 front ---
    q3 = Queue()
    emit("queue_front_empty", str(q3.front()))  # -1

    # --- enqueue + dequeue + size ---
    q4 = Queue()
    q4.enqueue(10)
    q4.enqueue(20)
    q4.enqueue(30)
    emit("queue_size_3", str(q4.queue_size()))  # 3
    q4.dequeue()
    emit("queue_size_after_dequeue", str(q4.queue_size()))  # 2

    # --- 多次 enqueue/dequeue 交替 ---
    q5 = Queue()
    q5.enqueue(1)
    q5.enqueue(2)
    emit("queue_alternate_dequeue_1", str(q5.dequeue()))  # 1
    q5.enqueue(3)
    emit("queue_alternate_front", str(q5.front()))  # 2
    emit("queue_alternate_dequeue_2", str(q5.dequeue()))  # 2
    emit("queue_alternate_dequeue_3", str(q5.dequeue()))  # 3
    emit("queue_alternate_size", str(q5.queue_size()))  # 0


if __name__ == "__main__":
    main()
