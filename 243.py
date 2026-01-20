s = "PAYPALISHIRING"

numRows = 4

length=len(s)

ans=""

dp=[""]*numRows
            
i=0

j=0

down=True

up=False

while i<length:
    dp[j]+=s[i]
    i+=1
    if down:
        if j<numRows-1:
            j+=1
        else:
            j-=1
            down=False
            up=True
    else:
        if j>0:
            j-=1
        else:
            j+=1
            down=True
            up=False
            
print("".join(dp))







def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [""] * numRows
    currRow = 0
    goingDown = False

    for ch in s:
        rows[currRow] += ch
        # flip direction at first or last row
        if currRow == 0 or currRow == numRows - 1:
            goingDown = not goingDown
        currRow += 1 if goingDown else -1

    return "".join(rows)
