def Winner(M, N):
	if (M % 2 == 0 or N % 2 == 0):
		return "Player 1"
	else:
		return "Player 2"
M,N=map(int,input().split())
print(Winner(M, N))


