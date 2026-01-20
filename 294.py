root = [1,2,3,4]

m=len(root)

ans=""
        
def tree(curr):
    global ans
    ans+=str(root[curr])
    if curr>=len(root)//2:
        return
    left=2*curr + 1
    right=2*curr + 2
    if left<m:
        ans+="(" 
        tree(left)
        ans+=")"
    if right<m:
        ans+="(" 
        tree(right)
        ans+=")"
        
tree(0)

print(ans)










root = [1,2,3,4]
m=len(root)

ans=""

def tree(curr):
    global ans
    
    ans += str(root[curr])
    
    left  = 2*curr + 1
    right = 2*curr + 2
    
    # if no children, just return
    if left >= m and right >= m:
        return
    
    # left subtree
    if left < m:
        ans += "("
        tree(left)
        ans += ")"
    else:
        # if left missing but right exists -> add empty ()
        ans += "()"
    
    # right subtree
    if right < m:
        ans += "("
        tree(right)
        ans += ")"

tree(0)
print(ans)