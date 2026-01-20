board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "ABCCED"

global flag
flag=False

def wordsearch(i,j,k,visited):
    global flag
    if k>=len(word)-1:
        flag=True
        print(True)
        return
    visited.add((i, j))
    if j>0 and (i,j-1) not in visited and board[i][j-1]==word[k+1]:
        wordsearch(i,j-1,k+1,visited)
    if j<len(board[0])-1 and (i,j+1) not in visited and board[i][j+1]==word[k+1]:
        wordsearch(i,j+1,k+1,visited)
    if i>0 and (i-1,j) not in visited and  board[i-1][j]==word[k+1]:
        wordsearch(i-1,j,k+1,visited)
    if i<len(board)-1 and (i+1,j) not in visited and board[i+1][j]==word[k+1]:
        wordsearch(i+1,j,k+1,visited)
    visited.remove((i, j))
    return
        
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]==word[0]:
            wordsearch(i,j,0,set())
            
print(flag)