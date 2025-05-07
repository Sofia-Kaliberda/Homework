arr = [0, 1, 7, 2, 4, 8]

result = 0
if arr:
    sum_even = 0
    for i in range(0, len(arr), 2):
        sum_even += arr[i]
    result = sum_even * arr[-1]
print("result:", result)