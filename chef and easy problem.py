

def pilesAndStones(arr,N):
	arr.sort(reverse=True)
	chef_count = 0
	roma_count = 0

	for i in range(N):
		if i % 2 == 0:
			chef_count += arr[i]
		else:
			roma_count += arr[i]

	return chef_count



for _ in range(int(input())):
	N = int(input())
	arr = list(map(int,input().split()))
	result = pilesAndStones(arr, N)
	print(result)
