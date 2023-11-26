'''
Objectives

    improving the student's skills in operating with the deepcopy() method on a list of dictionaries.

Scenario
Introduction

Imagine you have been hired to help run a candy warehouse.
The task

    Your task is to write a code that will prepare a proposal of reduced prices for the candies whose total weight exceeds 300 units of weight (we don’t care whether those are kilograms or pounds)
    Your input is a list of dictionaries; each dictionary represents one type of candy. Each type of candy contains a key entitled 'weight', which should lead you to the total weight details of the given delicacy. The input is presented in the editor;
    Prepare a copy of the source list (this should be done with a one-liner) and then iterate over it to reduce the price of each delicacy by 20% if its weight exceeds the value of 300;
    Present an original list of candies and a list that contains the proposals;
    Check if your code works correctly when copying and modifying the candy item details.
'''

import copy

warehouse = list()
warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})

# Execute the price proposal of 20% on weight over 300
proposal_warehouse = copy.deepcopy(warehouse)
for item in proposal_warehouse:
    if item['weight'] > 300:
        item['price'] *= 0.80


# Print both price lists
print('Source list of candies')
for item in warehouse:
    print(item)

print("******************")

print('Price proposal')
for item in proposal_warehouse:
    print(item)