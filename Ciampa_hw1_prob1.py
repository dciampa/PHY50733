num=int(input("Enter a number to convert to binary: "))
temp=num
bin=[]

while temp > 0:
	#Check modulus to see if the number is even or odd. If odd, put 1 for binary, if even put 0.
	rem=temp%2
	bin.append(rem)
	#Divide evaluted number by 2 with no remainder to run through again.
	temp=temp//2

#Binary number is in reverse due to how program iterated. This flips it.
bin.reverse()

#Output as single integer.
bin=int(''.join(map(str,bin)))
print(bin)