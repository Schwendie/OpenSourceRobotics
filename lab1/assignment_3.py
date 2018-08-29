import sys

if __name__ == "__main__":
	try:
		n = int(sys.argv[1])
	except:
		print("Please use an integer value")
		try:
			n = float(sys.argv[1])
			n = round(n)
		except:
			print("Using default value 1")
			n = 1

fact = 1

while n >= 1:
	fact = fact * n
	n-=1

print("\nFactorial for your number is ")
print(fact)