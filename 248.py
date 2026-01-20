def multiply(num1: str, num2: str) -> str:
    # If either is "0", answer is "0"
    if num1 == "0" or num2 == "0":
        return "0"
    
    n, m = len(num1), len(num2)
    res = [0] * (n + m)  # max possible digits
    
    # Reverse iteration from rightmost digits
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            # position in result array
            p1, p2 = i + j, i + j + 1
            # add to existing value
            total = mul + res[p2]
            
            res[p2] = total % 10
            res[p1] += total // 10
    
    # Convert to string, skipping leading zeros
    result = []
    for num in res:
        if not (len(result) == 0 and num == 0):
            result.append(str(num))
    
    return "".join(result) if result else "0"







def multiply_single(num: str, digit: str) -> str:
    if digit == "0":
        return "0"
    carry = 0
    d = ord(digit) - ord("0")
    res = []
    for i in range(len(num)-1, -1, -1):
        prod = (ord(num[i]) - ord("0")) * d + carry
        res.append(str(prod % 10))
        carry = prod // 10
    if carry:
        res.append(str(carry))
    return "".join(res[::-1])

def add_strings(a: str, b: str) -> str:
    i, j = len(a)-1, len(b)-1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        x = ord(a[i]) - ord("0") if i >= 0 else 0
        y = ord(b[j]) - ord("0") if j >= 0 else 0
        total = x + y + carry
        res.append(str(total % 10))
        carry = total // 10
        i -= 1
        j -= 1
    return "".join(res[::-1])

def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"
    ans = "0"
    m = len(num2)
    for i in range(m-1, -1, -1):
        partial = multiply_single(num1, num2[i])
        partial += "0" * (m-1-i)  # append zeros
        ans = add_strings(ans, partial)
    return ans