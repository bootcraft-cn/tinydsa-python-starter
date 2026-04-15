"""test_s04.py — S04 Array Deque test driver.

Provided by tinydsa-starter. Do NOT modify.
The tester runs this file to verify your ArrayDeque implementation.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from tinydsa import ArrayDeque


def emit(test_name: str, result: str) -> None:
    print(f"TEST:{test_name}")
    print(f"RESULT:{result}")


def arr_str(arr: list[int]) -> str:
    """Convert int list to comma-separated string for structured output."""
    return ",".join(str(x) for x in arr)


def main() -> None:
    # --- 基本操作 ---
    deque = ArrayDeque()
    emit("initial_size", str(deque.size()))  # 0

    # --- addLast ---
    deque.add_last(10)
    deque.add_last(20)
    deque.add_last(30)
    emit("to_array_after_add_last", arr_str(deque.to_array()))  # 10,20,30
    emit("size_after_add_last", str(deque.size()))  # 3

    # --- addFirst ---
    deque2 = ArrayDeque()
    deque2.add_first(30)
    deque2.add_first(20)
    deque2.add_first(10)
    emit("to_array_after_add_first", arr_str(deque2.to_array()))  # 10,20,30
    emit("size_after_add_first", str(deque2.size()))  # 3

    # --- 混合 addFirst/addLast ---
    deque3 = ArrayDeque()
    deque3.add_first(20)
    deque3.add_last(30)
    deque3.add_first(10)
    deque3.add_last(40)
    emit("to_array_mixed", arr_str(deque3.to_array()))  # 10,20,30,40
    emit("size_mixed", str(deque3.size()))  # 4

    # --- get（逻辑索引） ---
    emit("get_0", str(deque3.get(0)))  # 10
    emit("get_1", str(deque3.get(1)))  # 20
    emit("get_3", str(deque3.get(3)))  # 40
    emit("get_out_of_bounds", str(deque3.get(10)))  # -1
    emit("get_negative", str(deque3.get(-1)))  # -1

    # --- removeFirst ---
    deque4 = ArrayDeque()
    deque4.add_last(10)
    deque4.add_last(20)
    deque4.add_last(30)
    emit("remove_first_val", str(deque4.remove_first()))  # 10
    emit("size_after_remove_first", str(deque4.size()))  # 2
    emit("to_array_after_remove_first", arr_str(deque4.to_array()))  # 20,30

    # --- removeFirst 空队列 ---
    deque5 = ArrayDeque()
    emit("remove_first_empty", str(deque5.remove_first()))  # -1

    # --- removeLast ---
    deque6 = ArrayDeque()
    deque6.add_last(10)
    deque6.add_last(20)
    deque6.add_last(30)
    emit("remove_last_val", str(deque6.remove_last()))  # 30
    emit("size_after_remove_last", str(deque6.size()))  # 2
    emit("to_array_after_remove_last", arr_str(deque6.to_array()))  # 10,20

    # --- removeLast 空队列 ---
    deque7 = ArrayDeque()
    emit("remove_last_empty", str(deque7.remove_last()))  # -1

    # --- 交替 removeFirst/removeLast ---
    deque8 = ArrayDeque()
    deque8.add_last(10)
    deque8.add_last(20)
    deque8.add_last(30)
    deque8.add_last(40)
    emit("alternate_remove_first", str(deque8.remove_first()))  # 10
    emit("alternate_remove_last", str(deque8.remove_last()))  # 40
    emit("to_array_after_alternate", arr_str(deque8.to_array()))  # 20,30
    emit("size_after_alternate", str(deque8.size()))  # 2

    # --- 环绕测试（addFirst 造成 head 环绕） ---
    deque9 = ArrayDeque()
    deque9.add_last(10)
    deque9.add_last(20)
    deque9.add_last(30)
    deque9.add_first(5)
    deque9.add_first(1)
    emit("to_array_wraparound", arr_str(deque9.to_array()))  # 1,5,10,20,30
    emit("size_wraparound", str(deque9.size()))  # 5
    emit("get_0_wraparound", str(deque9.get(0)))  # 1
    emit("get_4_wraparound", str(deque9.get(4)))  # 30

    # --- 扩容测试（addLast 超过默认容量 8） ---
    deque10 = ArrayDeque()
    for i in range(1, 10):
        deque10.add_last(i)
    emit("to_array_after_resize", arr_str(deque10.to_array()))  # 1,2,3,4,5,6,7,8,9
    emit("size_after_resize", str(deque10.size()))  # 9
    emit("get_8_after_resize", str(deque10.get(8)))  # 9

    # --- 扩容测试（addFirst 超过默认容量 8） ---
    deque11 = ArrayDeque()
    for i in range(1, 10):
        deque11.add_first(i)
    emit("to_array_add_first_resize", arr_str(deque11.to_array()))  # 9,8,7,6,5,4,3,2,1
    emit("size_add_first_resize", str(deque11.size()))  # 9

    # --- 删空再添加 ---
    deque12 = ArrayDeque()
    deque12.add_last(10)
    deque12.add_last(20)
    deque12.remove_first()
    deque12.remove_last()
    emit("size_after_clear", str(deque12.size()))  # 0
    deque12.add_first(88)
    deque12.add_last(99)
    emit("to_array_after_refill", arr_str(deque12.to_array()))  # 88,99
    emit("size_after_refill", str(deque12.size()))  # 2

    # --- toArray 空队列 ---
    deque13 = ArrayDeque()
    emit("to_array_empty", arr_str(deque13.to_array()))  # (empty string)


if __name__ == "__main__":
    main()
