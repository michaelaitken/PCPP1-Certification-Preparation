# INCORRECT / NOT RECOMMENDED

try:
    print(1/0)
except Exception as e:
    pass


# CORRECT / RECOMMENDED

try:
    print(1/0)
except ZeroDivisionError:
    print("Don't divide by zero!")
    
# OR

try:
    number = int(input("Enter an integer number: "))
except:
    number = 0

