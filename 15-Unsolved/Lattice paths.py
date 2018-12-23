"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?

"""

x=(0,0)
y=(20,20)

for i in range(20):
    x[1]+=i
    for i in range(20):
        x[0]+=i