strings = input().split(", ")
nums = list(map(int, strings))

res = []
for i, v in enumerate(nums):
    if v % 2 == 0:
        res.append(i)

print(res)
