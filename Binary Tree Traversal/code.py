class Node():
    def __init__(self, val = 0, left = None, right = None):
        self.left = left
        self.right= right
        self.data = val
# Pre-order traversal
def pre_order(node):
    if node == None:
        return []
    listic = []
    listic.append(node.data)
    listic.extend(pre_order(node.left))
    listic.extend(pre_order(node.right))
    return listic

# In-order traversal
def in_order(node):
    if node == None:
        return []
    listic = []
    #ці умови з if не потрібні, але я залишила їх, бо такий скрін з тестом(щоб не були різні)
    if node.left:
        listic.extend(in_order(node.left))
    listic.append(node.data)
    if node.right:
        listic.extend(in_order(node.right))
    return listic

# Post-order traversal
def post_order(node):
    if node == None:
        return []
    listic = []
    listic.extend(post_order(node.left))
    listic.extend(post_order(node.right))
    listic.append(node.data)
    return listic
