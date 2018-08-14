#Raise Exception:
num = input(":")
if float(num) < 0:
 raise ValueError("Negative!")

#Other one example:
try:
   num = 5 / 0
except:
   print("An error occurred")
   raise
