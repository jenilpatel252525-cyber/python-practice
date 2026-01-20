version1="1.02.3.4.10"

version2="1.002.0003.4.10"

v1=version1.split(".")

v2=version2.split(".")

for i in range(max(len(v1),len(v2))):
    if i<len(v1) and i<len(v2):
        if int(v1[i])>int(v2[i]):
            print(1)
            break
        elif int(v1[i])<int(v2[i]):
            print(-1)
            break
    elif i>=len(v1):
        if int(v2[i])>0:
            print(-1)
            break
    elif i>=len(v2):
        if int(v1[i])>0:
            print(1)
            break
else:
    print(0)
    
    
    
    
    
    
    
def compareVersion(version1: str, version2: str) -> int:
    i, j = 0, 0
    n, m = len(version1), len(version2)
    
    while i < n or j < m:
        # extract number from version1
        num1 = 0
        while i < n and version1[i] != '.':
            num1 = num1 * 10 + int(version1[i])
            i += 1
        i += 1  # skip dot
        
        # extract number from version2
        num2 = 0
        while j < m and version2[j] != '.':
            num2 = num2 * 10 + int(version2[j])
            j += 1
        j += 1  # skip dot
        
        # compare current revision
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
    
    return 0