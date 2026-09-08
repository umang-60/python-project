import secrets
#password generator
print("========== random password generator ==========")
length=int(input("enter your length of password:"))
up=input("include uppercase letters?(y/n)").lower()
lp=input("include lowercase letters?(y/n)").lower()
numbers=input("include numbers (y/n)").lower()
special=input("include special characters (y/n)").lower()

#chacters groups
lowergroup="abcdefghijklmnopqrstuvwxyz"
uppergroup="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbergroup="1234567890"
specialgroup="!@#$%^&*_+<>?"

characters=""
required=[]
if up=="y":
    characters+=uppergroup
    required.append(secrets.choice(uppergroup))
if lp=="y":
    characters+=lowergroup
    required.append(secrets.choice(lowergroup))
if numbers=="y":
    characters+=numbergroup
    required.append(secrets.choice(numbergroup))
if(special=="y"):
    characters+=specialgroup
    required.append(secrets.choice(specialgroup))

password=""
if length < len(required):
    print("Password length is too short!")
else:
    #Add guaranteed characters first
    for char in required:
        password += char
    #Generate remaining characters
    remaining = length - len(required)
    for i in range(remaining):
        password += secrets.choice(characters)

    print("generated password: " + password)