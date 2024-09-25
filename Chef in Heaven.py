
def goHeaven(L,S):
	counter0 = 0
	counter1 = 0 
	for i in S:
		if i == '0':
			counter0 += 1
		elif i == '1':
			counter1 += 1
		if counter1 >= counter0:
			return 'Yes'

	if counter1 >= counter0:
		return('Yes')
	else:
		return('No')


for i in range(int(input())):
	L = int(input())
	lis = input()
	result = goHeaven(L,lis)
	print(result)
