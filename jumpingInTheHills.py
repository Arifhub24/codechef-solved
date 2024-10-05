

def jump(arr, count, D, U, P):
	if len(arr) == 1:
		return count
	if arr[1] > arr[0]:
		if arr[1] - arr[0] > U:
			return count
		pass
	elif arr[1] < arr[0]:
		if arr[0] - arr[1] > D:
			if P == False:
				return count
			else:
				P = False

	arr = arr[1:]
	count += 1
	return jump(arr, count, D, U, P)

	

for _ in range(int(input())):
	N, U, D = map(int,input().split())
	arr = list(map(int,input().split()))
	result = jump(arr, 1, D, U, True)
	print(result)
