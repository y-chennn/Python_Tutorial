numbers = [10, 8, 3, 22, 33, 7, 11, 100, 51]
numbers.sort()
x = 7

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2
    if numbers[mid] > x:
        high = mid - 1
    elif numbers[mid] < x:
        low = mid + 1
    else:
        break

print(numbers[mid], mid)