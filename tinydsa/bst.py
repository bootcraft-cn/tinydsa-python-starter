"""BST — 二叉搜索树（插入、查找、中序遍历）。

key 为 string 类型，value 为 int 类型。
BST 性质：左子树所有 key < 当前 key < 右子树所有 key。
"""


class BSTNode:
    """BST 节点。"""

    __slots__ = ("key", "val", "left", "right")

    def __init__(self, key: str, val: int) -> None:
        self.key: str = key
        self.val: int = val
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None


class BST:
    """二叉搜索树（key: string, value: int）。"""

    def __init__(self) -> None:
        self._root: BSTNode | None = None
        self._size: int = 0

    def put(self, key: str, val: int) -> None:
        """插入或更新键值对。"""
        raise NotImplementedError("TODO: S06")

    def get(self, key: str) -> int:
        """查找 key 对应的 value。不存在返回 -1。"""
        raise NotImplementedError("TODO: S06")

    def contains(self, key: str) -> bool:
        """判断 key 是否存在于树中。"""
        raise NotImplementedError("TODO: S06")

    def size(self) -> int:
        """返回树中键值对的个数。"""
        raise NotImplementedError("TODO: S06")

    def keys(self) -> list:
        """中序遍历，返回按字典序排列的所有 key 数组。"""
        raise NotImplementedError("TODO: S06")
