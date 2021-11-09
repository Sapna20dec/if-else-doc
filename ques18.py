science=int(input("enter science no"))
physics=int(input("enter the physics no"))
maths=int(input("enter the maths no"))
chemistry=int(input("enter the chemistry no"))
hindi=int(input("enter the hindi no"))
total_no=(science +physics+maths+chemistry+hindi)
per=(total_no)/500*100
if per>=90:
    print("a")
elif per>=80:
    print("b")
elif per>=70:
    print("c")
elif per>=60:
    print("d")
elif per>="40":
    print("e")
else:
    print("false")