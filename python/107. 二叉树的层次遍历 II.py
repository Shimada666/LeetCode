# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        WHITE, GRAY = 0, 1
        stack = []
        init_level = 0
        stack.append((root, WHITE, init_level))
        result = []
        while stack:
            node, color, level = stack.pop()
            if node:
                if color == WHITE:
                    stack.append((node.right, WHITE, level + 1))
                    stack.append((node.left, WHITE, level + 1))
                    stack.append((node, GRAY, level))
                else:
                    if len(result) == level:
                        result.append([])
                    result[level].append(node.val)
        return result[::-1]