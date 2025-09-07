class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}
        for index,value in enumerate(nums):
            # Chcek if number in hashmap and current index - hashmap[number]index<=k
            if value in hashmap and index-hashmap[value]<=k: 
                return True
            else:
                hashmap[value]=index # store that number:index pair in hashmap
        return False # if no duplicates exist