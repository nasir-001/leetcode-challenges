class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val,
        self.left = left,
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.right)
                    q.append(node.left)

            if level:
                result.append(level)

        return result