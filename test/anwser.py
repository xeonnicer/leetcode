# nums = input()
# heights = list(map(int, input().split()))
# print(heights)
# friends = [0 for i in nums]
# for i in range(nums):
#     if i == nums - 1:
#         break
#     for j in range(i + 1, nums - 1):
#         if heights[j] > heights[i]:
#             friends[i] = j
#             break
# print((for i in friends))
# heights = list(map(int, input().split()))


# nums = list(map(int, input().strip().split()))
# nums.sort()
# str_nums=''.join(str(i) for i in nums)
# print(type(nums))
# print(len(nums))
# print(type(str_nums))
# for i in nums:
#     str_nums.lstrip('0')
# print(str_nums)


# nums = list(map(int, input().strip().split()))
# nums.sort()
# str_nums=''.join(str(i) for i in nums)
# print(str_nums.lstrip('0'))


# nums = input().strip().split()
# nums.sort(key=lambda x: sum(ord(i) for i in x), reverse=True)
# str_nums = ''.join(str(i) for i in nums)
# print(str_nums.lstrip('0'))
#
# x = '999'


# nums = input().strip().strip('}').split()
# nums.sort(key=lambda x: sum(ord(i) for i in x))
# str_nums=''.join(str(i) for i in nums)
# print(str_nums.lstrip('0'))


# a = ['1999', '99', '996', '9961', '0']

# nums = input().strip().strip('}').split()
nums = '996 9961 99 9 0 8 808 909 111 009'.split()
max_length = max( len(i) for i in nums)
# nums.sort(key=lambda x: sum(ord(i) for i in x))
def key(x):
    return int(x.ljust(max_length, '9'))
nums.sort(key=key, reverse=True)
str_nums=','.join(str(i) for i in nums)
print(str_nums)
