
# BECAREFUL OF THIS!!

def fun(x=0, y=0, z=0, a=1, b=2, c=3):
    pass

# It looks the same, but isn't
fun(1, 2, 3)
fun(a=1, b=2, c=3)


# ALSO...
# What will be printed??
print("A" > "a")
print(1.0 == 1)
print("1" == 1)
print(True == "1")
print(True == 1)
print(True == 1.0)
print("1" + "1")
print(1 + 1)
print(1 + "1")