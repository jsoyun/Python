# 트리를 순회하는 문제
# postorder방식으로 순회
# 나의 자식들 먼저 방문하고 나를 방문

def LCA(root, p, q):
    if root == None:
        return None

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right


LCA([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4)
