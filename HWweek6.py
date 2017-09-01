class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isequal(rootS, rootT):
    if rootS is None and rootT is None:
        return True
    if rootS is None or rootT is None:
        return False
    return rootS.val == rootT.val and isequal(rootS.left, rootT.left) and isequal(rootS.right, rootT.right)
    
def isSubtree(s, t):
    if s is None:
        return False
    if t is None:
        return False
    if (isequal(s, t)):
        return True
    return isSubtree(s.left, t) or isSubtree(s.right, t)

#Test 1
T = TreeNode(4)
T.left = TreeNode(1)
T.right = TreeNode(2)

S = TreeNode(3)
S.right = TreeNode(5)
S.left = TreeNode(4)
S.left.left = TreeNode(1)
S.left.right = TreeNode(2)

print isSubtree(S, T)

#Test 2
T = TreeNode(4)
T.left = TreeNode(1)
T.right = TreeNode(2)

S = TreeNode(3)
S.right = TreeNode(5)
S.left = TreeNode(4)
S.left.left = TreeNode(1)
S.left.right = TreeNode(2)
S.left.right.left = TreeNode(0)
print isSubtree(S, T)

#Test 3
T = TreeNode(4)
T.left = TreeNode(1)
T.right = TreeNode(2)

S = TreeNode(4)
S.left = TreeNode(1)
S.right = TreeNode(2)
print isSubtree(S, T)

#Test 4
T = TreeNode(3)
T.right = TreeNode(5)
T.left = TreeNode(4)
T.left.left = TreeNode(1)
T.left.right = TreeNode(2)

S = TreeNode(4)
S.left = TreeNode(1)
S.right = TreeNode(2)
print isSubtree(S, T)

#Test 5
T = TreeNode(None)
S = TreeNode(None)
print isSubtree(S, T)

#Test 6
T = TreeNode(1)
S = TreeNode(1)
print isSubtree(S, T)

#Test 7
T = TreeNode(None)
S = TreeNode(1)
print isSubtree(S, T)



