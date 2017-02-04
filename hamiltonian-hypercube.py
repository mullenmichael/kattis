#
# hamiltonian-hypercube.py
# NWERC 2016
# Michael Mullen
# 04/02/17
#


# Get the index of a binary code
# Interestingly, does not depend on dimension
def ind(x):
    # Base Case
    if len(x) == 1:
        return int(x)

    # Recursive step
    if x[0] == '0':
        return ind(x[1:])
    else:
        return 2**len(x) - ind(x[1:]) - 1


# Get input
n,a,b = input().split()

# Convert inputs to their correct types
n = int(n)
a = str(a)
b = str(b)

# Distance between each index
dist = ind(b) - ind(a) - 1

# Output the solution
print(dist)

