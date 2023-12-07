foods = ['pizza', 'hotdog', 'spaghetti', 'hamburger']

# O(1)
# n = 0
# print(foods[0])

# O(n)
# for food in foods:
#     if food == 'pizza':
#         print(food)
#         break
#     else:
#         print('not find')

# O(log n)
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