s = "aabca"
n = len(s)
results = []
print(s, n)

def isPalindrome(path):
    left, right = 0, len(path) - 1

    while left < right:
        if path[left] != path[right]:
            return False
        left += 1
        right -= 1
    return True


def backtrack(start_index, path):
    global n
    print("start_index: ", start_index, "path: ", path)
    if start_index > n:
        print("> than n")
        return
    if len(path) == 3:
        print("len of 3")
        if isPalindrome(path):
            results.append(path[:])
        return
    
    if len(path) > 3:
        return
    
    for i in range(start_index, n):
        path.append(s[i])
        backtrack(i+1, path)
        path.pop()
backtrack(0, [])
print(results)