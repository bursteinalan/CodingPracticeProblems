def problem1(n):
	'''
	Time Complexity: n*sqrt(n)
	'''
	square_root=0
	squares = []
	while square_root**2<n:
		squares.append(square_root**2)
		square_root+=1

	results = [0]
	j=1
	for i in range(1,n+1):
		if i==j**2:
			results.append(1)
			continue
		j=1
		min_num = 1+results[i-1]
		while j**2 < i:
			min_num = min(min_num,1+results[i-squares[j]])
			j+=1
		results.append(min_num)
	return results[n]

def problem2(n):
	'''
	'''
	a=1

def main():
	# p1_1 = problem1(12)
	# p1_2 = problem1(13)
	# print('p1_1 should be 3 and is:',p1_1)
	# print('p1_2 should be 2 and is:',p1_2)
    p2_1 = problem2("23")
    p2_1_ans = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print('p2_1 should be',p2_1_ans,' and is:',p2_1)

main()


