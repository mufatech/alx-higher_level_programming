#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid in non-attacking positions
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for j in range(n):
        a.append([j, None])

    def already_exists(y):
        """check that a queen does not already exist in that z value"""
        for y in range(n):
            if z == a[y][1]:
                return True
        return False

    def reject(y, z):
        """determines whether or not to reject the solution"""
        if (already_exists(z)):
            return False
        j = 0
        while(j < y):
            if abs(a[j][1] - z) == abs(j - y):
                return False
            j += 1
        return True

    def clear_a(y):
        """clears the answers from the point of failure on"""
        for j in range(y, n):
            a[j][1] = None

    def nqueens(y):
        """recursive backtracking function to find the solution"""
        for z in range(n):
            clear_a(y)
            if reject(y, z):
                a[y][1] = z
                if (y == n - 1):  # accepts the solution
                    print(a)
                else:
                    nqueens(y + 1)  # moves on to next y value to continue

    # start the recursive process at y = 0
    nqueens(0)
