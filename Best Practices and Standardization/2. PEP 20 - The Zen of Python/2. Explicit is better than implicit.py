
# INCORRECT / NOT RECOMMENDED
from fruit import *

apples(2, 3.45)


# CORRECT / RECOMMENDED
from fruit import apples, bananas

apples(quantity=2, price=3.45)