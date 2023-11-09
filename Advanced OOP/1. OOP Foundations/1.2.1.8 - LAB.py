import random

# Global Values
NUMBER_OF_APPLES = 1000
WEIGHT_LIMIT = 300

# Class Definition
class Apple:
    apples_processed = 0
    total_weight = 0
    
    def __init__(self):
        self.weight = random.uniform(0.2, 0.5)
        Apple.apples_processed += 1
        Apple.total_weight += self.weight

# List of Apples
apple_box = []

# Create all the apples and append to the list
while Apple.apples_processed < NUMBER_OF_APPLES and Apple.total_weight < WEIGHT_LIMIT:
    apple_box.append(Apple())

# Check if Apple count was reached
if Apple.apples_processed == NUMBER_OF_APPLES and Apple.total_weight <= WEIGHT_LIMIT:
    print(f"Succesfully packed {Apple.apples_processed} apples! Totalling {round(Apple.total_weight, 2)} units")
else:
    print(f"Packing stopped at {Apple.apples_processed} apples packed! Totalling {round(Apple.total_weight, 2)} units")