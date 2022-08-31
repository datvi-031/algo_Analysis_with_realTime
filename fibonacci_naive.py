# for measuring time taken by algorithm (time module to get current time)
import time

# store the begin time
begin = time.time()

def fibRecurse(num):
	""" recursive function for calculating nth fibonnoci number"""
	if num<=1:
		return num
	return fibRecurse(num-1)+fibRecurse(num-2)

# prints docstring in fibRecurse()
print(">> recursive approach: ", fibRecurse.__doc__)

num = int(input("Enter the n: "))
print("{}th fibonocci number: {}".format(num, fibRecurse(num)))

# holds the program for 1sec from execution
time.sleep(1)

# store the end time
end = time.time()

# print the time taken 
print("Alorithmic time: ", end-begin)

# what am i doing here
# 1. Store the starting time before the first line of the program executes.
# 2. Store the ending time after the last line of the program executes.
# 3. Print the difference between start time and end time.