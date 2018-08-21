#filter:-
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)


#Other example of filter:
nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x<5,nums))print(res)
