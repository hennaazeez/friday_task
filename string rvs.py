b = input("Enter the string : ")
rev = ""
for i in range(len(b),0,-1):
    rev = rev + b[i-1]
print("Reverse of string is :",rev)