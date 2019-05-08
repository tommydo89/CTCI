# A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree. 

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)
Node2.left = Node1
Node2.right = Node3

# def weaveLists(list1, list2, prefix, results):
#     # base case - If either list is empty, append the other remaining list onto the prefix and store it into our results array
#     if (len(list1) == 0 or len(list2) == 0):
#         results.append(prefix + list1 + list2)
#         return
#     prefixL1 = prefix[:]
#     prefixL1.append(list1[0])
#     weaveLists(list1[1:], list2, prefixL1, results)
#     prefixL2 = prefix[:]
#     prefixL2.append(list2[0])
#     weaveLists(list1, list2[1:], prefixL2, results)

def weaveLists(list1, list2, prefix, results):
    # base case - If either list is empty, append the other remaining list onto the prefix and store it into our results array
    if (len(list1) == 0 or len(list2) == 0):
        results.append(prefix + list1 + list2)
        return
    weaveLists(list1[1:], list2, prefix + [list1[0]], results)
    weaveLists(list1, list2[1:], prefix + [list2[0]], results)


def BSTSequences(node):
    # base case 
    if (node == None):
        return [[]]
    # if the node is not None, then recurse on the left and right. The return value will be a list of all the possible sequences for each left and right subtree
    leftSeq = BSTSequences(node.left)
    rightSeq = BSTSequences(node.right)
    prefix = [node.val]
    results = []
    # We weave each list of sequences from the left and right subtree and then prepend it with root node by setting the root node to be the prefix
    for seqL in leftSeq:
        for seqR in rightSeq:
            weaved = weaveLists(seqL, seqR, prefix, results)
    # results now contains the list of sequences that could lead to the tree rooted at the current iteration's node
    return results




