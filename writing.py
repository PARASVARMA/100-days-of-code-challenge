#Write Files:-
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()
file = open("newfile.txt", "r")
print(file.read())
file.close()

#Other examples of writing files
file = open("newfile.txt", "r")
print("Reading initial oontents")
print(file.read())
print("finished")
file.close()

#writer method for returns the number of bytes:-
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

