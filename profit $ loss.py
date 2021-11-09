i=0
while i<100:
    if i%7==0 or i%5==0:
        print("navguukul")
    if i%5==0:
        print("nav")
    if i%7==0:
        print("guru")
    i=i+1   




selling_prize=int(input("enter the number"))
if selling_prize>50:
    print("profit")
elif selling_prize<50:
    print("loss")
else:
    print("no profit no loss")
