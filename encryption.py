a = input("what is the message you want to encrypt")
b = int(input("what do you want to change the code"))

new=""

for i in a:
    c = ord(i)+b
    new = new + str(c) + "."
print(new)