class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dict={}
        for num in nums:
            if num in dict: #num la irrukurathu dictla irrukurathu value irrunchuna true 
                return True

            dict[num]=1 #step 1:-new values create panrom key and value example {2:1} step2:{2:1,3:1} step 3:-(2:1,3:1,4:1)
        return False

        