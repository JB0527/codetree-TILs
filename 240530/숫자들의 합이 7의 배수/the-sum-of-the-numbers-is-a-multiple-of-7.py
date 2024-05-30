n = int(input())
arr = [int(input()) for i in range(n)]
'''
#누적합으로 풍어야함
tmp = 0
for i,value in enumerate(arr):
    if  value % 7 == 0:
        tmp += 1
        arr.pop(i)

def finding(arr):
    answer = 0
    find = arr.pop()
    for j,value in enumerate(arr):
        if (find + j) % 7 == 0:
            answer += 2
            arr.pop(j)
    return answer
answers = 0
while len(arr) >= 1:
    answers += finding(arr)
#print(arr)
print(answers+tmp)
'''
def max_subarray_size_divisible_by_7(numbers):
    n = len(numbers)
    prefix_sums = [0] * (n + 1)
    
    # Calculate prefix sums
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + numbers[i - 1]

    # Dictionary to store the first occurrence of each remainder
    remainder_map = {}
    max_size = 0

    for i in range(n + 1):
        remainder = prefix_sums[i] % 7
        
        if remainder in remainder_map:
            # Calculate the size of the subarray
            size = i - remainder_map[remainder]
            max_size = max(max_size, size)
        else:
            # Store the first occurrence of the remainder
            remainder_map[remainder] = i

    return max_size

# Example usage

print(max_subarray_size_divisible_by_7(arr))  # Output: 5