from collections import deque
# class Node:
#     def __init_(self, L, R, n):
#         self.left = L
#         self.right = R
#         self.value = n
def tree_by_levels(node):
    if node == None:
        return []
    listic = []
    level = deque()
    level.append(node)
    while level:
        curr = level.popleft()
        listic.append(curr.value)
        if curr.left:
            level.append(curr.left)
        if curr.right:
            level.append(curr.right)
    return listic
    