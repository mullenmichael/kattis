#
# free-weights.py
# NWERC 2016
# Michael Mullen
# 31/01/17
#
# Key to Solution: the weights can be paired correctly by 
# removing a certain weight if, by removing all other
# weights <= current weight, the rows are paired properly 
#

# Function to check if a row has each of its weights paired correctly
def checkRow(row):
    # If there's only one weight left on the row, it hasn't been paired correctly
    if len(row) == 1:
        return False
    # If there are no weights on the row, that's fine 
    elif len(row) == 0:
        return True
    
    i = 1
    while i < len(row):
        if row[i] != row[i-1]:
            return False
        else:
            i += 2

    # If we've got this far, row must be correctly paired
    return True

def BinSearch(weights):

    # Base Case
    if len(weights) == 1:
        # If only one weight left, it must work
        # so return it
        return weights[0]

    # Get the middle index of the weights list
    med = len(weights) // 2

    # Create rows of all weights less than the median weight
    row_one = [x for x in rows[0] if x > weights[med]]
    row_two = [x for x in rows[1] if x > weights[med]]

    # Check if constraints satisfied
    if checkRow(row_one) and checkRow(row_two):
        # works for this, check if there is a lower case that works
        return min(weights[med], BinSearch(weights[med:]))
    else:
        # doesn't work for this (therefore, nothing lower
        # than this as well), so check for the higher
        return BinSearch(weights[:med])

unique_weights = set()
rows = []

# Get inputs
num_pairs = int(input())

NUM_ROWS = 2
for i in range(NUM_ROWS):
   
    row_list = []  # List of weights on this row

    # Take in input for individual weights, adding them to the set as needed
    for x in input().split():
        weight = int(x)
        
        if weight not in unique_weights:
            unique_weights.add(weight)  # add each weight to the set of unique weights 

        row_list.append(weight)

    # Append the entire row to the rows list
    rows.append(row_list)

# Convert set to a list so it can be sorted
unique_weights = list(unique_weights)

# Include a zero case (already every pair matched)
unique_weights.append(0)

# Sort weights backwards so they can be binary searched (bs later)
unique_weights.sort(reverse=True)

smallest_correct_weight = BinSearch(unique_weights)
print(smallest_correct_weight)
