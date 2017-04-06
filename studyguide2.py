# study guide exam 2

# Lecture Notes on 19 Feb 2016

# determine the sum of the proper divisors of a number
def sum_divisors (n):
  sum_div = 0
  limit = n // 2
  div = 1
  while (div <= limit):
    if (n % div == 0):
      sum_div += div
    div += 1
  return sum_div

# determine if a number is prime
def is_prime (n):
  if (n == 1):
    return False

  limit = int(n ** 0.5) + 1
  divisor = 2
  while (divisor < limit):
    if (n % divisor == 0):
      return False
    divisor += 1
  return True

# determine if a number is palindromic
def is_palindromic (n):
  return (n == rev_num(n))

# reverse a number
def rev_num (n):
  rev_n = 0
  while (n > 0):
    rev_n = rev_n * 10 + (n % 10)
    n = n // 10
  return rev_n

# sum the digits of a number
def sum_digits (n):
  sum_num = 0
  while (n > 0):
    sum_num = sum_num + (n % 10)
    n = n // 10
  return sum_num

# compute the cycle length of a number using Collatz condition
def compute_cycle_length (n):
  cycle_length = 0
  while (n > 1):
    if (n % 2 == 0):
      n = n // 2
    else:
      n = 3 * n + 1
    cycle_length = cycle_length + 1
  return cycle_length

def main():
  # prompt the user to enter a number
  num = eval (input ("Enter number: "))

  # call the function compute_cycle_length
  cycle_length = compute_cycle_length (num)

  # print the result
  print ("For the number " + str(num) + " the cycle length is " + str(cycle_length))

  # sum the digits of a number
  sum_d = sum_digits (num)
  print (sum_d)

  # reverse a number
  rev_n = rev_num (num)
  print (rev_n)

  # print all prime number less than 50
  num = 2
  limit = 50
  while (num < limit):
    if (is_prime(num)):
      print (num)
    num = num + 1


  # print all perfect numbers less than 10000
  num = 1
  while (num <= 10000):
    if (num == sum_divisors(num)):
      print (num)
    num += 1


  # print all 3 digit emirps
  # an emirp is a non-palindromic prime which when reversed is prime
  num = 100
  while (num <= 999):
    if (is_prime(num) and not is_palindromic(num)):
      if (is_prime (rev_num(num))):
        print (num)
    num += 1

  # print 4-digit non-palindromic number whose cube is palindromic
  num = 1000
  while (num <= 9999):
    if (not is_palindromic (num)):
      num3 = num * num * num
      if (is_palindromic (num3)):
        print (num)
    num += 1

main()

# Lecture Notes on 06 Apr 2016

def end(s):
	for ch in a:
		print(ch, end=' ')
	print()

def max_num (a):
  max_n = a[0]
  for i in range (1, len(a)):
    if (a[i] > max_n):
      max_n = a[i]
  return max_n

def min_num (a):
  min_n = a[0]
  for i in range (1, len(a)):
    if (a[i] < min_n):
      min_n = a[i]
  return min_n

def max_prod (a):
  max_p = a[0] * a[1]
  for i in range (1, len(a) - 1):
    prod = a[i] * a[i + 1]
    if (prod > max_p):
      max_p = prod
  return max_p

def is_sorted (a):
  for i in range (0, len(a) - 1):
    if (a[i] > a[i + 1]):
      return False
  return True

def sum_num (a):
  sum_n = 0
  for i in range (len(a)):
    sum_n += a[i]
  return sum_n

def pascal():
	
	it=2
	print(1)
	while it<10:
		a=[1,1]
		b=[1]
		while len(b)<len(a)+1:
			b.append(it)

def binary_search (a, x):
  lo = 0
  hi = len(a) - 1

  while (lo <= hi):
    mid = (lo + hi) // 2
    if (x > a[mid]):
      lo = mid + 1
    elif (x < a[mid]):
      hi = mid - 1
    else:
      return mid
  return -1

def seq_search (a, x):
  for i in range (len(a)):
    if (a[i] == x):
      return i
  return -1		

def files():

	file = open('example.txt','r')

	a=[]
	b=[]

	for i in file:
		a.append(i)

	for i in a:
		if i=='\n':
			a.remove(i)

	for i in a:
		b.append(i.replace('pedo','onda'))

	out=open('outexample.txt','w')

	for i in b:
		out.write(i)

	out.close()

def is_palindromicstr(s):
	st=''
	for i in range(len(s)-1,-1,-1):
		st+=s[i]

	if st==s:
		return True
	else:
		return False

def rotation(s,n):
	st=''

	for i in range(len(s)-n,len(s)):
		st+=s[i]
	st+=s[:len(s)-n]

	return st

def occurrences(f,s):

	file = open(f,'r')

	a=[]

	for i in file:
		a.append(i)

	file.close()

	b=[]

	for i in a:
		b.append(i.count(s))

	return sum(b)

def forbidden(f,s):

	file = open(f,'r')

	a=[]

	for i in file:
		a.append(i)

	file.close()

	b=[]

	for i in a:
		b=i.split()
		for j in b:
			if j==s:
				return False
		b=[]

	return True

def sumlist(a,b):
	s=0
	for i in range(len(a)):
		s+=a[i]*b[i]
	return s

def sortlist(a):
	for i in range(len(a)-1):
		if a[i]>a[i+1]:
			return False
	return True

def sort3(a):
	if a[0]>a[2]:
		a[2],a[0]=a[0],a[2]
	if a[0]>a[1]:
		a[0],a[1]=a[1],a[0]
	if a[1]>a[2]:
		a[1],a[2]=a[2],a[1]
	return a

def shuffle(a):
	import random
	b=[]
	it=0
	while len(a)>0:
		b.append(random.choice(a))
		a.remove(b[it])
		it+=1
	return b

def secondhighest(a):
	maxnum=max(a)
	a.remove(maxnum)
	second=max(a)
	while second==maxnum:
		a.remove(max(a))
		second=max(a)
	return second























			




