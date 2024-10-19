# Given an array of distinct positive integers 'candidates' and a target integer 'target', return a list of all unique combinations of 'candidates' where the chosen numbers sum to 'target'. You may return the combinations in any order.

# The same number may be chosen from 'candidates' an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# Example 1:

# Input: candidates = [2, 3, 6, 7], target = 7  
# Output: [[2, 2, 3], [7]]
# Explanation: The elements in these two combinations sum up to 7.


# Example 2:

# Input: candidates = [2, 4, 6, 8], target = 10  
# Output: [[2,2,2,2,2], [2,2,2,4], [2,2,6], [2,4,4], [2,8], [4,6]]    
# Explanation: The elements in these six combinations sum up to 10.
candidates = [2, 4, 6, 8]
target = 10
results = []

# [2, 2, 2, 2] 8

def backtrack(start_index, path):
    global target
    global candidates
    if sum(path) == target:
        results.append(path[:])
        return
    if sum(path) > target:
        return
    
    # traversal logic
    for i in range(start_index, len(candidates)):
        if candidates[i] + sum(path) > target:
            break # skip [2,2,2,3...]
        path.append(candidates[i])
        backtrack(i, path)
        path.pop()

backtrack(0, [])
print(results)
