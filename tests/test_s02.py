"""test_s02.py — S02 Singly Linked List test driver.

Provided by tinydsa-starter. Do NOT modify.
The tester runs this file to verify your SinglyLinkedList implementation.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from tinydsa import SinglyLinkedList


def emit(test_name: str, result: str) -> None:
    print(f"TEST:{test_name}")
    print(f"RESULT:{result}")


def arr_str(arr: list[int]) -> str:
    """Convert int list to comma-separated string for structured output."""
    return ",".join(str(x) for x in arr)


def main() -> None:
    # --- 基本操作 ---
    sll = SinglyLinkedList()
    emit("initial_size", str(sll.size()))  # 0

    # --- addFirst ---
    sll.add_first(30)
    sll.add_first(20)
    sll.add_first(10)
    emit("size_after_3_add_first", str(sll.size()))  # 3
    emit("to_array_after_add_first", arr_str(sll.to_array()))  # 10,20,30

    # --- addLast ---
    sll2 = SinglyLinkedList()
    sll2.add_last(10)
    sll2.add_last(20)
    sll2.add_last(30)
    emit("to_array_after_add_last", arr_str(sll2.to_array()))  # 10,20,30

    # --- 混合 addFirst/addLast ---
    sll3 = SinglyLinkedList()
    sll3.add_first(20)
    sll3.add_last(30)
    sll3.add_first(10)
    emit("to_array_mixed", arr_str(sll3.to_array()))  # 10,20,30
    emit("size_mixed", str(sll3.size()))  # 3

    # --- get ---
    emit("get_0", str(sll3.get(0)))  # 10
    emit("get_1", str(sll3.get(1)))  # 20
    emit("get_2", str(sll3.get(2)))  # 30
    emit("get_out_of_bounds", str(sll3.get(5)))  # -1
    emit("get_negative", str(sll3.get(-1)))  # -1

    # --- removeFirst ---
    sll4 = SinglyLinkedList()
    sll4.add_last(10)
    sll4.add_last(20)
    sll4.add_last(30)
    emit("remove_first_val", str(sll4.remove_first()))  # 10
    emit("size_after_remove_first", str(sll4.size()))  # 2
    emit("to_array_after_remove_first", arr_str(sll4.to_array()))  # 20,30

    # --- removeFirst 空链表 ---
    sll5 = SinglyLinkedList()
    emit("remove_first_empty", str(sll5.remove_first()))  # -1

    # --- removeLast ---
    sll6 = SinglyLinkedList()
    sll6.add_last(10)
    sll6.add_last(20)
    sll6.add_last(30)
    emit("remove_last_val", str(sll6.remove_last()))  # 30
    emit("size_after_remove_last", str(sll6.size()))  # 2
    emit("to_array_after_remove_last", arr_str(sll6.to_array()))  # 10,20

    # --- removeLast 空链表 ---
    sll7 = SinglyLinkedList()
    emit("remove_last_empty", str(sll7.remove_last()))  # -1

    # --- removeLast 连续至空 ---
    sll8 = SinglyLinkedList()
    sll8.add_last(10)
    sll8.add_last(20)
    sll8.add_last(30)
    emit("remove_last_3", str(sll8.remove_last()))  # 30
    emit("remove_last_2", str(sll8.remove_last()))  # 20
    emit("remove_last_1", str(sll8.remove_last()))  # 10
    emit("size_after_remove_all", str(sll8.size()))  # 0
    emit("remove_last_when_empty", str(sll8.remove_last()))  # -1

    # --- 删空再添加 ---
    sll9 = SinglyLinkedList()
    sll9.add_first(10)
    sll9.add_first(20)
    sll9.remove_first()
    sll9.remove_first()
    emit("size_after_clear", str(sll9.size()))  # 0
    sll9.add_last(99)
    emit("get_after_refill", str(sll9.get(0)))  # 99
    emit("size_after_refill", str(sll9.size()))  # 1

    # --- toArray 空链表 ---
    sll10 = SinglyLinkedList()
    emit("to_array_empty", arr_str(sll10.to_array()))  # (empty string)


if __name__ == "__main__":
    main()
