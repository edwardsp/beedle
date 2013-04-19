import collections

def mean(X):
	n = len(X)
	if n > 0:
		return float(sum(X)) / float(len(X))
	return 0


def median(X):
	n = len(X)
	if n == 0:
		return 0
	L = sorted(X)
	if n % 2:
		# odd number of elements
		return L[n/2]
	return mean(L[(n/2)-1:(n/2)+1])


def mode(X):
	n = len(X)
	if n == 0:
		return []
	S = collections.Counter(X).most_common()
	freq = S[0][1]
	return [ S[i][0] for i in range(len(S)) if S[i][1] == freq ]


