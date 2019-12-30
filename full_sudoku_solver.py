import numpy as np

board=np.array([[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0]])

bo1=np.array([[1,1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1,1]])

#sudoku question
qboard=np.array([[8,0,0,0,0,0,0,0,0],
				 [0,0,3,6,0,0,0,0,0],
				 [0,7,0,0,9,0,2,0,0],
				 [0,5,0,0,0,7,0,0,0],
				 [0,0,0,0,4,5,7,0,0],
				 [0,0,0,1,0,0,0,3,0],
				 [0,0,1,0,0,0,0,6,8],
				 [0,0,8,5,0,0,0,1,0],
				 [0,9,0,0,0,0,4,0,0]])
				 
sparse=np.array([[1,0,0,0,0,0,0,0,0],
				 [0,1,0,0,0,0,0,0,0],
				 [0,0,1,0,0,0,0,0,0],
				 [0,0,0,1,0,0,0,0,0],
				 [0,0,0,0,1,0,0,0,0],
				 [0,0,0,0,0,1,0,0,0],
				 [0,0,0,0,0,0,1,0,0],
				 [0,0,0,0,0,0,0,1,0],
				 [0,0,0,0,0,0,0,0,1]])
				 
#No solution
nosol=np.array([[0,2,3,0,9,8,0,0,0],
				[9,8,7,4,5,6,0,0,0],
				[4,5,6,2,3,7,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0]])
N=9				

#check horizontal
def checkhor(board,row,num):
	for x in range(9):
		if board[row][x]==num:
			return True
			
	return False

#check vertical
def checkvert(board,col,num):
	for y in range(N):
		if board[y][col]==num:
			return True
			
	return False

#check square
def checksquare(board,row,col,num):
	for x in range(3):
		for y in range(3):
			if board[row+y][col+x]==num:
				return True
	
	return False


#combined function for checking number
def canplace(board,row,col,num):
	if checkhor(board,row,num)==False and checkvert(board,col,num)==False and checksquare(board,row-row%3,col-col%3,num)==False:
		return True
		
	else:
		return False


#function for finding blank, *tentative
def findblank(board):
	for i in range(N):
		for j in range(N):
			if board[i][j]==0:
				return i,j


#solve function
def solve(board):
	#set end conditions
	if findblank(board)==None:
		return True
		
	row=findblank(board)[0]
	col=findblank(board)[1]
		
	for n in range(1,10):
		if canplace(board,row,col,n)==True:
			board[row][col]=n
			print(board)
			if solve(board)==True:
				return True
	
		board[row][col]=0
				
	return False

def showsolve(board):
	if solve(board)==True:
		print(board,'yaay')
	elif solve(board)==False:
		print('No solution')
	else:
		print('code got problem')
		
showsolve(qboard)
