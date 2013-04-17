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
	return mean(L[(n/2)-1:2])


def mode(X):
	n = len(X)
	if n == 0:
		return 0
	if n == 1:
		return X[0]
	S = collections.Counter(X).most_common()

	if S[0][1] == S[1][1]:
		return 0
			
	return S[0][0]


