class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: int, q: int) -> int:
    """
    Approach: classic recursive LCA — if current node is p or q, return it.
    Recurse left and right; if both sides return non-null, current node
    is the split point (LCA). Otherwise propagate whichever side is non-null.
    Time: O(n) — may visit every node once. Space: O(h) recursion stack.
    Edge case handled: single-node tree where p == q == root.val.
    """
    if root is None:
        return None
    if root.val == p or root.val == q:
        return root.val

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left is not None and right is not None:
        return root.val
    return left if left is not None else right
