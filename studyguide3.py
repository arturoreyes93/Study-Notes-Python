#StudyGuide Exam 3
# random.uniform(a,b) >> floating
# random.randint(a,b)
# random.shuffle(list)

import random 

def p1(st):
	# Get rid of whitespace at the beginning and end
	st = st.strip()
	# Get rid of spaces
	st = st.replace(" ", "")
	st = st.replace("\n", "")

	d = {}
	# Go through each character in the string
	for ch in st:
		# If ch is already a key in d
		if ch in d:
			# Increment the frequency of that ch value
			d[ch] += 1
		# If ch is NOT already a key in d
		else:
			# Add ch to the dictionary and set its frequency to 1
			d[ch] = 1
	print(d)
	return d

# Swap keys with values in a dictionary
def p2(d):
	# Create an empty dictionary
	d2 = {}

	for key in d:
		d2[d[key]] = key

	return d2

def p3(a, b):
	s1 = set(a)
	s2 = set(b)

	return list(s1 & s2)

def p4():
	l2d = []
	# 3 rows
	for i in range(3):
		l1d = []
		# 5 columns
		for j in range(5):
			l1d.append(random.uniform(1,100))
		l2d.append(l1d)

	return l2d
# Test if two 2d lists are equal
def p5(a, b):
	if len(a) != len(b):
		return False

	if len(a[0]) != len(b[0]):
		return False

	# Go through the rows
	for i in range(len(a)):
		# Go through the columns
		for j in range(len(a[0])):
			if (a[i][j] != b[i][j]):
				return False

	return True
	
def p6(a, b):
	c = []
	# Go through the rows
	for i in range(len(a)):
		l1d = []
		# Go through the columns
		for j in range(len(a[0])):
			l1d.append(a[i][j] + b[i][j])
		c.append(l1d)

	return c

# Reverse rows
def p7(a):
	# 1 2 3
	# 4 5 6

	# 3 2 1
	# 6 5 4
	b = []
	for i in range(len(a)): # Rows
		l1d = []
		for j in range(len(a[0])-1, -1, -1): # Columns in reverse order
			l1d.append(a[i][j])
		b.append(l1d)

	print(b)

	return b

# Reverse columns
def p8(a):
	b = a[:] # Make a copy of a
	b.reverse() # Reverse the outside 1d list
	
	print(b)
	return b


# Dot product
def p9(a, b):
	total = 0
	for i in range(len(a)):
		total += a[i] * b[i]
	return total

# Is sorted?
def p10(a):
	for i in range(len(a)-1):
		if a[i] > a[i+1]:
			return False
	return True

# Helper functions
def sum_rows(a):
	# Will return a list of sum of each row
	sums = []
	for row in a: # Each row
		rowtotal = 0 # Reset sum for each row
		for elem in row: # Each elem of each row
			rowtotal += elem

		sums.append(rowtotal) # Append each total

	return sums

def sum_cols(a):
	# Will return a list of sum of each col
	sums = []
	for j in range(len(a[0])): # Col
		total = 0
		for i in range(len(a)): # Row
			total += a[i][j]
		sums.append(total)

	return sums

def sum_main_diag(a):
	total = 0
	for i in range(len(a)):
		total += a[i][i]

	return total

def p11(a):
	sr = sum_rows(a)
	sc = sum_cols(a)
	sd = sum_diags(a)

	print("Sum rows: ", sr)
	print("Sum cols: ", sc)
	print("Sum main diag: ", sd)

def p12(a):
	# a only has 3 elements
	# If 1st > 2nd swap
	if a[0] > a[1]:
		a[1], a[0] = a[0], a[1]

	# If 2nd > 3rd swap
	if a[1] > a[2]:
		a[2], a[1] = a[1], a[2]

	# If 1st > 2nd swap
	if a[0] > a[1]:
		a[1], a[0] = a[0], a[1]

def p13(a):
	# If we shuffle
	return random.shuffle(a)

	# # If we rotate
	# rotate_val = random.randint(1,len(a))

	# return a[rotate_val:] + a[:rotate_val]

def p14(st1, st2):
	for ch1 in st1:
		if ch1.isalpha(): # If it's a letter
			if st1.count(ch1) != st2.count(ch1):
				return False
	for ch2 in st2:
		if ch2.isalpha():
			if st1.count(ch2) != st2.count(ch2):
				return False

	return True

def p14_take2(st1, st2):
	l1 = []
	l2 = []
	for ch in st1:
		if ch.isalpha():
			l1.append(ch)
	for ch in st2:
		if ch.isalpha():
			l2.append(ch)

	l1.sort()
	l2.sort()

	return l1 == l2

def p15(username, password):
	f = open("passwd.txt", "r")
	for line in f:
		line = line.strip() # Get rid of \n
		# unpw is an array of length 2
		# element 0 is username
		# element 1 is password
		unpw = line.split(":") 
		if username == unpw[0] and password == unpw[1]:
			f.close()
			return True

	f.close()
	return False

# DONE BY ME

def freq(st):

	s = st.split()

	freq_dict = {}

	for word in s:

		for ch in word:

			if ch in freq_dict:

				freq_dict[ch] = freq_dict[ch] + 1

			else:

				freq_dict[ch] = 1

	print (freq_dict)

def flip_dict1(dictionary):

	my_dict = dictionary

	new_dict = dict (zip(my_dict.values(),my_dict.keys()))

	print(new_dict)

def flip_dict2(dictionary):

	dic = dictionary

	dic2 = {}

	for i in dic:

		dic2[dic[i]] = i

	print(dic2)

def create_2dlist():

	import random

	grid = []

	for i in range(3):

		row = []

		for j in range(5):

			row.append(random.randint(1,100))

		grid.append(row)

	print(grid)

def sumlist(a,b):

	c = []

	for i in range(len(a)):

		row = []

		for j in range(len(a[i])):

			row.append(a[i][j]+b[i][j])

		c.append(row)

	print(c)

def reverse_row(a):

	for i in range(len(a)):

		a[i].reverse()

	print(a)

def reverse_column(a):

	b = []

	for i in range((len(a)-1),-1,-1):

		b.append(a[i])

	print(b)

def prodlist(a,b):

	s = 0

	for i in range(len(a)):

		s += a[i]*b[i]

	print(s)

def ascending(a):

	for i in range(len(a)-1):

		if a[i] > a[i+1]:

			return False

	return True

def sumrows(a):

	rowsums = []

	for i in a:

		rowsums.append(sum(i))

	print(rowsums)

	return rowsums

def sumcols(a):

	colsums = []

	for i in range(len(a[0])):

		s = 0

		for j in range(len(a)):

			s += a[j][i]

			colsums.append(s)

	print(colsums)

	return colsums

def sort3(a):
	if a[0]>a[2]:
		a[2],a[0]=a[0],a[2]
	if a[0]>a[1]:
		a[0],a[1]=a[1],a[0]
	if a[1]>a[2]:
		a[1],a[2]=a[2],a[1]
	return a

def anagrams(s1,s2):
	s1 = s1.lower()
	s2 = s2.lower()

	st1 = []
	st2 = []

	for ch in s1:
		if ch.isalpha() :
			st1.append(ch)

	for ch in s2:
		if ch.isalpha():
			st2.append(ch)

	st1 = set(st1)
	st2 = set(st2)

	if st1 == st2:
		print('True')
		return True
	else:
		print('False')
		return False

def id(username,password):

	file = open('passwd.txt','r')

	listp = []

	for line in file:

		line.strip()
		line.replace('\n','')

		listp.append(line)

	if username == listp[0] and password == listp[1]:
		print('True')
	else:
		print('False')



def main():

	a = 'Arturo es chingon. Todos lo saben'
	b = 'arTurO e,s chingon; todo.s lo sabEn'

	c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	sum_rows(c)
	sumrows(c)




	

main()
