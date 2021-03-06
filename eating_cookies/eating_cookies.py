import math
from functools import lru_cache
'''
Input: an integer
Returns: an integer
'''
@lru_cache(maxsize=1000)
def eating_cookies(n):
    # Your code here
    if n < 0:
        return 0
    if n == 0:
        return 1
    answer = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    return answer



        

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 35

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
