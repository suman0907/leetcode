class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        for i in range(len(nums2)):
            mp[nums2[i]]=i
        result = []    
        for i in range(len(nums1)):
            index = mp[nums1[i]]
            flag = -1
            for j in range(index+1,len(nums2)):
                if nums1[i]<nums2[j]:
                    flag = nums2[j]
                    break
            result.append(flag)  
        return result              
        