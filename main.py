def has_good_pair(arr, target_sum):
    n = len(arr)
    seen = set()
    for num in arr:
        if target_sum - num in seen:
            return 1
        seen.add(num)
    return 0
A = [1,2,3,4]
B = 7
result = has_good_pair(A, B)
print("Does a good pair exist?", result)
A = [1,2,4]
B = 4
result = has_good_pair(A, B)
print("Does a good pair exist?", result)
A = [1,2,2]
B = 4
result = has_good_pair(A, B)
print("Does a good pair exist?", result)
