import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1,n2):
            if int(n1+n2)>int(n2+n1):
                return 1
            elif int(n1+n2)<int(n2+n1):
                return -1
            return 0
        nums = [str(n) for n in nums]
        nums = sorted(nums,key= functools.cmp_to_key(compare),reverse=True)
        ans = '0' if nums[0]=='0' else ''.join(nums)
        return ans    

        