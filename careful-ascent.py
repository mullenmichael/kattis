# Careful Ascent
# NWERC 16
# Michael Mullen
# 20/11/2016
#

# Get input
x, y = map(int, input().split())
n = int(input())

tot_y_dist = 0
tot_x_dist = 0

for i in range(n):
    start, end, factor = map(float, input().split())

    # Update y-distance travelled
    tot_y_dist += end - start

    # Update actual x-distance travelled
    tot_x_dist += (end - start) * factor

vx = (x * 1.0)/((y - tot_y_dist) + tot_x_dist)

print vx
