"""test_s01.py — S01 Dynamic Array test driver.

Provided by tinydsa-starter. Do NOT modify.
The tester runs this file to verify your DynamicArray implementation.
"""

import os
import sys

# Ensure tinydsa is importable regardless of how this script is invoked
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from tinydsa import DynamicArray


def emit(test_name: str, result: str) -> None:
    print(f"TEST:{test_name}")
    print(f"RESULT:{result}")


def main() -> None:
    # --- 基本操作 ---
    arr = DynamicArray()
    emit("initial_size", str(arr.size()))           # 0
    emit("initial_capacity", str(arr.capacity()))   # 8

    # --- add + get ---
    arr.add(10)
    arr.add(20)
    arr.add(30)
    emit("size_after_3_adds", str(arr.size()))       # 3
    emit("get_0", str(arr.get(0)))                   # 10
    emit("get_1", str(arr.get(1)))                   # 20
    emit("get_2", str(arr.get(2)))                   # 30

    # --- get 越界 ---
    emit("get_out_of_bounds", str(arr.get(5)))       # -1
    emit("get_negative", str(arr.get(-1)))           # -1

    # --- set ---
    arr.set(1, 99)
    emit("get_after_set", str(arr.get(1)))           # 99
    arr.set(100, 42)  # 越界，不操作
    emit("size_after_oob_set", str(arr.size()))      # 3

    # --- 扩容 ---
    arr2 = DynamicArray()
    for i in range(8):
        arr2.add(i)
    emit("cap_before_expand", str(arr2.capacity()))  # 8
    arr2.add(8)  # 第 9 个元素触发扩容
    emit("cap_after_expand", str(arr2.capacity()))   # 16
    emit("size_after_expand", str(arr2.size()))       # 9
    emit("get_8_after_expand", str(arr2.get(8)))     # 8

    # --- 扩容后数据完整性 ---
    intact = True
    for i in range(9):
        if arr2.get(i) != i:
            intact = False
            break
    emit("data_intact_after_expand", str(intact).lower())  # true

    # --- removeAt 基本 ---
    arr3 = DynamicArray()
    arr3.add(10)
    arr3.add(20)
    arr3.add(30)
    arr3.add(40)
    removed = arr3.remove_at(1)
    emit("removeAt_return", str(removed))             # 20
    emit("size_after_remove", str(arr3.size()))        # 3
    emit("get_1_after_remove", str(arr3.get(1)))       # 30 (左移)
    emit("get_2_after_remove", str(arr3.get(2)))       # 40

    # --- removeAt 越界 ---
    emit("removeAt_oob", str(arr3.remove_at(10)))     # -1

    # --- 缩容 ---
    arr4 = DynamicArray()
    for i in range(16):
        arr4.add(i)
    emit("cap_16_elements", str(arr4.capacity()))     # 16

    # 连续删除至 size < capacity/4
    for _ in range(13):
        arr4.remove_at(arr4.size() - 1)
    emit("size_after_removes", str(arr4.size()))       # 3
    emit("cap_after_shrink", str(arr4.capacity()))     # 8 (16 → 8, 不低于 8)

    # --- 缩容后数据完整性 ---
    emit("get_0_after_shrink", str(arr4.get(0)))       # 0
    emit("get_1_after_shrink", str(arr4.get(1)))       # 1
    emit("get_2_after_shrink", str(arr4.get(2)))       # 2

    # --- 删空再添加 ---
    arr5 = DynamicArray()
    arr5.add(1)
    arr5.add(2)
    arr5.remove_at(0)
    arr5.remove_at(0)
    emit("size_empty", str(arr5.size()))               # 0
    arr5.add(100)
    emit("get_after_refill", str(arr5.get(0)))         # 100
    emit("size_after_refill", str(arr5.size()))         # 1


if __name__ == "__main__":
    main()
