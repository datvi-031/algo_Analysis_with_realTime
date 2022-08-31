import time
begin = time.time()

li = list()
li.append(0)
li.append(1)

def fibonacci_better(num):
	"""calculates nth fibonocci number iterative and store way(in list)"""
	for i in range(1, num):
		li.append(li[i-1]+li[i])
	return li[-1]

# prints the doc string inside fibonacci_better
print(">> iterative and store aproach: ", fibonacci_better.__doc__)

num = int(input("Enter n: "))
print("{}th fibonocci number: {}".format(num, fibonacci_better(num)))

time.sleep(1)
end = time.time()
print("Alorithmic time: ", end-begin)