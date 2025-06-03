def dfs(self, index, curr, Sum, candidates, target, res):
    if index == len(candidates):
        return
    
    if Sum > target:
        return 
    
    if Sum == target:
        res.append(curr.copy())
        return
    
    curr.append(candidates[index])
    self.dfs(index, curr, Sum + candidates[index], candidates, target, res)
    curr.pop()
    self.dfs(index + 1, curr, Sum, candidates, target, res)


def combinationSum(self, candidates, target):
    res = []
    curr = []
    index = 0
    Sum = 0

    self.dfs(index, curr, Sum, candidates, target, res)
    
    return res

candidates = list(map(int, input().split()))
target = int(input())
print(combinationSum(candidates, target))

"""
----- Pick & Not Pick Approach -----

combinationSum(candidates, target):
* This is the main function.

- res to store the final result (list of valid combinations).

- curr to store the current combination being built.

- index and Sum to track position and current sum.

It calls the dfs function to start the backtracking search.

dfs(index, curr, Sum, candidates, target, res):
* This is the recursive function (depth-first search with backtracking).

Base cases:

1. If Sum == target: We found a valid combination → add a copy of curr to res.

2. If Sum > target or we've gone past the end (index == len(candidates)): stop exploring this path.

Recursive steps:

- Include the current number (candidates[index]) and call dfs again without moving the index (since we can reuse the same number).

- Backtrack by removing the last number added (curr.pop()).

- Exclude the current number and move to the next index (index + 1).
"""