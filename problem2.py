import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:  # If the number is odd
        print("Weird")
    else:  # The number is even
        if 2 <= n <= 5:  # Even number between 2 and 5
            print("Not Weird")
        elif 6 <= n <= 20:  # Even number between 6 and 20
            print("Weird")
        elif n > 20:  # Even number greater than 20
            print("Not Weird")
        
