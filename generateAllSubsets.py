def generateAllSubsets(nums):
        res = []
        n = len(nums)
        subset = 1 << n # 2^n = total number of subsets possible

        for num in range(subset): # 0 to possible number of subsets
            lst = []
            for i in range(n): # for each bit
                if num & (1 << i):
                    lst.append(nums[i])
            res.append(lst)
        return res

nums = list(map(int, input("Enter input list (space separated): ").split()))
print(generateAllSubsets(nums))

"""
Problem: Generate all subsets (power set) for give list of unique integers.

Concept Used: The function uses bit manipulation to generate the power set, which has 2^n subsets for a list of length n.

Explanation:
* n is the number of elements in the input list nums.
* 1 << n performs a left bit shift which calculates 2^n — total number of subsets.
* Each number from 0 to 2^n - 1 represents a unique subset (each bit tells whether to include an element from nums).
* Check the 'i'th bit of the current number num.
*num & (1 << i) checks if the ith bit is set (i.e., 1).
    * If yes, include nums[i] in the current subset lst.
* After constructing the subset lst, it's added to the final result list res.

"""