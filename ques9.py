# char=input("enter the character")

# if (char>="a" and char<="z") or (char>"A" and char<="Z"):
#     print("aphabet hai")
# elif (char>=0 and char<=9):
#     print("integer hai") 
# elif  (char=="@","$","#","&","%"):
#     print("special character hai") 







char=input("enter a character")
same=("#","@","%","&","$")
if (char>="a" and char<="z") or (char>"A" and char<="z"):
    print("alphabet")
elif char in same :
    print("special character")
else:
    print('digit number')