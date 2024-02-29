"""
Name: Bradyn Combs
Lab Time: 2/22/24 2:00 PM
"""

def fibonacci(n):
    #write your code here
    global c
    c = 0
    a = 0
    b = 1

    for i in range(1,n):
        c = a + b
        a = b
        b = c

    if n < 0:
        c = -1
    return c

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')