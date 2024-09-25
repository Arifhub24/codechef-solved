


def count_tibes(S):
	before = ''
	current_count = 0
	count_A = 0
	count_B = 0

	for element in S:
		if element == 'A':
			if before == 'A':
				count_A += current_count + 1
				current_count = 0
			else:
				count_A += 1
				current_count = 0
				before = 'A'

		elif element == 'B':
			if before == 'B':
				count_B += current_count + 1
				current_count = 0
			else:
				count_B += 1
				current_count = 0
				before = 'B'
		else:
			current_count += 1

	print(count_A,count_B)

for _ in range(int(input())):
	S = input()
	count_tibes(S)

