#list introduction
number = 3
things = ["string", 0, [1, 2, number],4.56]
print(things[1])
print(things[2])
print(things[2][2])

#list operation
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)   #lists and strings are similar in many ways


#Other list operation to check if an item is in a list or not
words = ["sapm", "egg", "spam", "sausage"]
print("sausage" in words)
print("tomato" in words)

#example of lists: -
nums = [10, 9, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])
