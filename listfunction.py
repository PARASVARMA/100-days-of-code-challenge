#list append function:-
words = ["hello"]
words.append("world")
print(words[1])

#list len function:-
nums = [1, 3, 5, 7, 9]
print(len(nums))

#other len function example:
letters = ["a", "b", "c"]
letters.append("d")
print(len(letters))

#list insert function:-
words = ["python", "fun"]
index = 1
words.insert(index, "is")
print(words)

#other insert function example:-
nums = [9, 4, 3, 2, 1]
nums.append(4)
nums.insert(2, 11)
print(len(nums))

#list index function:-
letters = ['p', 'q', 'r', 's', 't']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('z'))