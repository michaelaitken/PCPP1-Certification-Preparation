
# INCORRECT / NOT RECOMMENDED
from math import sqrt
sidea = float(input("The length of the 'a' side:"))
sideb = float(input("The length of the 'b' side:"))
sidec = sqrt(sidea**2+sideb**2)
print("The length of the hypotenuse is", sidec )


# CORRECT / RECOMMENDED
from math import sqrt

sidea = float(input("The length of the 'a' side:"))
sideb = float(input("The length of the 'b' side:"))
sidec = sqrt(sidea**2+sideb**2)

print("The length of the hypotenuse is", sidec )