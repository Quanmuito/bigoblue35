# https://www.hackerrank.com/challenges/minimum-loss/problem
# Complexity:
# - searchUpperboundNode: O(log N)
# - insertNode: O(log N)
# - Overall: O(N log N)

class Node:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None

def insertNode(root, x):
    if root == None: return Node(x)

    if x < root.key:
        root.left = insertNode(root.left, x)
    elif x > root.key:
        root.right = insertNode(root.right, x)

    return root

def searchUpperboundNode(root, x):
    if root == None:
        return root

    if root.key <= x:
        return searchUpperboundNode(root.right, x)

    upperBound = searchUpperboundNode(root.left, x)
    return upperBound if upperBound != None else root

n = int(input())
A = list(map(int, input().split()))

minLoss = int(1e16)
root = None

for price in A:
    buy = searchUpperboundNode(root, price)
    if buy != None:
        minLoss = min(minLoss, buy.key - price)

    root = insertNode(root, price)

print(minLoss)