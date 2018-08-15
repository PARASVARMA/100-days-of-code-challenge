#Reading files:-
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

#other examples:-
file = open("test.txt")
cont = file.read()
print(cont)
file.close()

#To read only a certain amount of a file
file = open("filename.txt","r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

#other one example:-
file = open("filename.txt","r")
str = file.read()
print(len(str))
file.close()

