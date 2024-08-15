class Solution(object):
    def threeSum(self, nums):
        results=[]
        nums.sort()
        #[-4,-3,-3,0,1,2,3,5,8]
        for i in range(len(nums)):
            if nums[i]==nums[i-1] and i>0:
                continue
            if nums[i]<=0:
                l1 = i
                r = len(nums)-1
                l2 = i + 1
                while l2<r:
                    if nums[l1] + nums[l2] + nums[r]>0:
                        r-=1
                    elif nums[l1] + nums[l2] + nums[r]<0:
                        l2+=1
                    else:
                        results.append([nums[l1],nums[l2],nums[r]])
                        l2+=1
                        while nums[l2]==nums[l2-1] and l2<r:
                            l2+=1
            else:
                break
        return results
        