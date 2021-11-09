age=int(input("enter the age"))
sex=input("enter a sex")
day=int(input("enter the day"))
if age>=18 and  age<=30:
    if sex=='m':
        print(day*700,"m")
    elif sex=='f':
        print(day*750,"f")
elif age>=30 and age<=40:
    if sex=="m":
        print(day*800)
    elif sex=="f":
        print(day*850)
else:
    print("enter appropriate age")

    