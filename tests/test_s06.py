# test_s06.py — S06 BST: Search & Insert test driver
# Provided by tinydsa-starter. Do NOT modify.

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from tinydsa.bst import BST


def emit(test_name: str, result: str) -> None:
    print(f"TEST:{test_name}")
    print(f"RESULT:{result}")


def main() -> None:
    # --- Group 1: Empty tree ---
    bst = BST()
    emit("bst_empty_size", str(bst.size()))
    emit("bst_empty_get", str(bst.get("any")))
    emit("bst_empty_contains", str(bst.contains("any")).lower())
    emit("bst_empty_keys", ",".join(bst.keys()))

    # --- Group 2: Single insert ---
    bst2 = BST()
    bst2.put("hello", 42)
    emit("bst_single_size", str(bst2.size()))
    emit("bst_single_get", str(bst2.get("hello")))
    emit("bst_single_contains", str(bst2.contains("hello")).lower())
    emit("bst_single_missing", str(bst2.contains("world")).lower())

    # --- Group 3: Multiple inserts + in-order keys ---
    bst3 = BST()
    bst3.put("dog", 3)
    bst3.put("cat", 1)
    bst3.put("elk", 5)
    bst3.put("ant", 2)
    bst3.put("bee", 4)
    emit("bst_multi_size", str(bst3.size()))
    emit("bst_multi_keys", ",".join(bst3.keys()))
    emit("bst_multi_get_first", str(bst3.get("ant")))
    emit("bst_multi_get_last", str(bst3.get("elk")))

    # --- Group 4: Update existing key ---
    bst3.put("cat", 999)
    emit("bst_update_get", str(bst3.get("cat")))
    emit("bst_update_size", str(bst3.size()))
    emit("bst_update_keys", ",".join(bst3.keys()))

    # --- Group 5: Get/contains edge cases ---
    emit("bst_get_missing", str(bst3.get("zzz")))
    emit("bst_contains_existing", str(bst3.contains("dog")).lower())
    emit("bst_contains_missing", str(bst3.contains("fox")).lower())

    # --- Group 6: Left-skewed tree ---
    bst4 = BST()
    bst4.put("e", 5)
    bst4.put("d", 4)
    bst4.put("c", 3)
    bst4.put("b", 2)
    bst4.put("a", 1)
    emit("bst_left_keys", ",".join(bst4.keys()))
    emit("bst_left_size", str(bst4.size()))
    emit("bst_left_get", str(bst4.get("a")))

    # --- Group 7: Right-skewed tree ---
    bst5 = BST()
    bst5.put("a", 1)
    bst5.put("b", 2)
    bst5.put("c", 3)
    bst5.put("d", 4)
    bst5.put("e", 5)
    emit("bst_right_keys", ",".join(bst5.keys()))
    emit("bst_right_size", str(bst5.size()))
    emit("bst_right_get", str(bst5.get("e")))

    # --- Group 8: Large tree ---
    bst6 = BST()
    bst6.put("m", 13)
    bst6.put("g", 7)
    bst6.put("t", 20)
    bst6.put("d", 4)
    bst6.put("j", 10)
    bst6.put("p", 16)
    bst6.put("w", 23)
    bst6.put("b", 2)
    bst6.put("f", 6)
    bst6.put("n", 14)
    emit("bst_large_size", str(bst6.size()))
    emit("bst_large_keys", ",".join(bst6.keys()))
    emit("bst_large_get", str(bst6.get("j")))
    emit("bst_large_contains", str(bst6.contains("n")).lower())

    # --- Group 9: Mixed operations ---
    bst7 = BST()
    bst7.put("x", 100)
    bst7.put("y", 200)
    bst7.put("x", 300)
    bst7.put("z", 400)
    emit("bst_mixed_overwrite", str(bst7.get("x")))
    emit("bst_mixed_final_size", str(bst7.size()))


if __name__ == "__main__":
    main()
