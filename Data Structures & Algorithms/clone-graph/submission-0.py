"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        copyDict = {}
        queue = deque()
        queue.append(node)
        copyDict[node] = Node(node.val)

        while queue:
            qnode = queue.popleft()
            for neighbor in qnode.neighbors:
                if neighbor not in copyDict:
                    n = Node(neighbor.val)
                    copyDict[neighbor] = n
                    queue.append(neighbor)
                copyDict[qnode].neighbors.append(copyDict[neighbor])

        return copyDict[node]