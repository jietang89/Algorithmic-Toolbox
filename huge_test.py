def sum(n):
	seq = [0,1]
	if n > 1:
		for i in range(2,n+1):
			seq.append((seq[i-1]+seq[i-2]+1)%10)

	return (seq)


# assert(n <= 45 & n>= 0)


print(sum(100))