import sys

def downtriangle(n, t=0):
    if n == 0:
        return 0
    else:
        print(' ' * ( t + 1 ) + '*' * ( n * 2 - 1 ))
        return downtriangle( n - 1, t + 1 )

downtriangle(int(sys.argv[1]))
