nums
#{1: 'one', 2: 'two', 3: 'three'}
for i in nums:
    print(i)
for i in nums:
    print(nums[i])
'''
one
two
three
'''


n = nums.items()
n
#dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
for key, value in nums.items():
    print(key, 'is', value)
'''
is one
is two
is three
'''


v_nums = []
for v in nums.values():
    v_nums.append(v)
v_nums
#['one', 'two', 'three']