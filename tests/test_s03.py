"""test_s03.py — S03 Doubly Linked List test driver.

Provided by tinydsa-starter. Do NOT modify.
The tester runs this file to verify your DoublyLinkedList implementation.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from tinydsa import DoublyLinkedList


def emit(test_name: str, result: str) -> None:
    print(f"TEST:{test_name}")
    print(f"RESULT:{result}")


def arr_str(arr: list[int]) -> str:
    """Convert int list to comma-separated string for structured output."""
    return ",".join(str(x) for x in arr)


def main() -> None:
    # --- 基本操作 ---
    dll = DoublyLinkedList()
    emit("initial_size", str(dll.size()))  # 0

    # --- addFirst ---
    dll.add_first(30)
    dll.add_first(20)
    dll.add_first(10)
    emit("size_after_3_add_first", str(dll.size()))  # 3
    emit("to_array_after_add_first", arr_str(dll.to_array()))  # 10,20,30
    emit("to_array_reverse_after_add_first", arr_str(dll.to_array_reverse()))  # 30,20,10

    # --- addLast ---
    dll2 = DoublyLinkedList()
    dll2.add_last(10)
    dll2.add_last(20)
    dll2.add_last(30)
    emit("to_array_after_add_last", arr_str(dll2.to_array()))  # 10,20,30
    emit("to_array_reverse_after_add_last", arr_str(dll2.to_array_reverse()))  # 30,20,10

    # --- 混合 addFirst/addLast ---
    dll3 = DoublyLinkedList()
    dll3.add_first(20)
    dll3.add_last(30)
    dll3.add_first(10)
    dll3.add_last(40)
    emit("to_array_mixed", arr_str(dll3.to_array()))  # 10,20,30,40
    emit("to_array_reverse_mixed", arr_str(dll3.to_array_reverse()))  # 40,30,20,10
    emit("size_mixed", str(dll3.size()))  # 4

    # --- get ---
    emit("get_0", str(dll3.get(0)))  # 10
    emit("get_1", str(dll3.get(1)))  # 20
    emit("get_3", str(dll3.get(3)))  # 40
    emit("get_out_of_bounds", str(dll3.get(10)))  # -1
    emit("get_negative", str(dll3.get(-1)))  # -1

    # --- removeFirst ---
    dll4 = DoublyLinkedList()
    dll4.add_last(10)
    dll4.add_last(20)
    dll4.add_last(30)
    emit("remove_first_val", str(dll4.remove_first()))  # 10
    emit("size_after_remove_first", str(dll4.size()))  # 2
    emit("to_array_after_remove_first", arr_str(dll4.to_array()))  # 20,30
    emit("to_array_reverse_after_remove_first", arr_str(dll4.to_array_reverse()))  # 30,20

    # --- removeFirst 空链表 ---
    dll5 = DoublyLinkedList()
    emit("remove_first_empty", str(dll5.remove_first()))  # -1

    # --- removeLast ---
    dll6 = DoublyLinkedList()
    dll6.add_last(10)
    dll6.add_last(20)
    dll6.add_last(30)
    emit("remove_last_val", str(dll6.remove_last()))  # 30
    emit("size_after_remove_last", str(dll6.size()))  # 2
    emit("to_array_after_remove_last", arr_str(dll6.to_array()))  # 10,20
    emit("to_array_reverse_after_remove_last", arr_str(dll6.to_array_reverse()))  # 20,10

    # --- removeLast 空链表 ---
    dll7 = DoublyLinkedList()
    emit("remove_last_empty", str(dll7.remove_last()))  # -1

    # --- 交替 removeFirst/removeLast ---
    dll8 = DoublyLinkedList()
    dll8.add_last(10)
    dll8.add_last(20)
    dll8.add_last(30)
    dll8.add_last(40)
    emit("alternate_remove_first", str(dll8.remove_first()))  # 10
    emit("alternate_remove_last", str(dll8.remove_last()))  # 40
    emit("to_array_after_alternate", arr_str(dll8.to_array()))  # 20,30
    emit("to_array_reverse_after_alternate", arr_str(dll8.to_array_reverse()))  # 30,20
    emit("size_after_alternate", str(dll8.size()))  # 2

    # --- removeLast 连续至空 ---
    dll9 = DoublyLinkedList()
    dll9.add_last(10)
    dll9.add_last(20)
    dll9.add_last(30)
    emit("remove_last_3", str(dll9.remove_last()))  # 30
    emit("remove_last_2", str(dll9.remove_last()))  # 20
    emit("remove_last_1", str(dll9.remove_last()))  # 10
    emit("size_after_remove_all", str(dll9.size()))  # 0
    emit("remove_last_when_empty", str(dll9.remove_last()))  # -1

    # --- 删空再添加（哨兵不被破坏） ---
    dll10 = DoublyLinkedList()
    dll10.add_first(10)
    dll10.add_last(20)
    dll10.remove_first()
    dll10.remove_last()
    emit("size_after_clear", str(dll10.size()))  # 0
    dll10.add_last(99)
    dll10.add_first(88)
    emit("to_array_after_refill", arr_str(dll10.to_array()))  # 88,99
    emit("to_array_reverse_after_refill", arr_str(dll10.to_array_reverse()))  # 99,88
    emit("size_after_refill", str(dll10.size()))  # 2

    # --- toArray / toArrayReverse 空链表 ---
    dll11 = DoublyLinkedList()
    emit("to_array_empty", arr_str(dll11.to_array()))  # (empty string)
    emit("to_array_reverse_empty", arr_str(dll11.to_array_reverse()))  # (empty string)


if __name__ == "__main__":
    main()
