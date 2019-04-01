#!/usr/bin/python

import random

def in_circle(x_in, y_in):
    LHS = (x_in - 0.5) ** 2 + (y_in - 0.5) ** 2
    RHS = 0.5 ** 2
    if LHS > RHS:
        return False
    return True

def picalc(n):
    inside_sum = 0

    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if in_circle(x,y):
            inside_sum += 1

    return(4 * inside_sum / n)

def main():
    n = input("Enter a number: ")
    out = picalc(int(n))
    print("Pi approximation: " + str(out))

if __name__ == "__main__":
    main()
