# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(start,end):
        # Base Case
            if start==end:
                return None
        # Calculate the mid and make mid value as the root
            mid=(start+end)//2
            root=TreeNode(nums[mid])
            root.left=build_tree(start,mid)
            root.right=build_tree(mid+1,end)
            return root
        return build_tree(0,len(nums))