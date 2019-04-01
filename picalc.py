#!/usr/bin/python

import random

def in_circle(x_in, y_in):
    term1 = (x_in - 0.5) ** 2
    term2 = (y_in - 0.5) ** 2
    if term1 + term2 > 0.25:
        return False
    return True

def picalc(n):
    inside_sum = 0
    outside_sum = 0

    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        result = in_circle(x, y)
        if result:
            inside_sum += 1
        else:
            outside_sum += 1
    return(4 * inside_sum / n)

def main():
    n = input("Enter a number: ")
    out = picalc(int(n))
    print("Pi approximation: " + str(out))

if __name__ == "__main__":
    main()



