"""
# Day 10 
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

"""
import time 

def f():
    print("function called")

def jobScheduler(f,n):
    n /= 1000
    time.sleep(n)
    f()

def main():
    jobScheduler(f,500)

if __name__ == "__main__":
    while True:
        main()