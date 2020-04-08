from collections import Counter

n = 9
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
pairCount = 0

for values in Counter(arr).values():
    pairCount += values//2
print(pairCount)

# def check(val):
#     pc = 0
#     for elem in arr:
#         if elem == val:
#             pc += 1
#     return pc

# for val in arr:
#     pairCount = check(val)

# print(pairCount)
# count = dict((i, ar.count(i)) for i in ar)