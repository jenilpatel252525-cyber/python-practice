def intToRoman(num: int) -> str:
    ans = ""
    num_str = str(num)
    length = len(num_str)
    
    for i in range(length-1, -1, -1):
        j = int(num_str[length - i - 1])
        
        if i == 3:  # Thousands place
            ans += "M" * j
        elif i == 2:  # Hundreds place
            if j == 9:
                ans += "CM"
            elif j >= 5:
                ans += "D" + "C" * (j - 5)
            elif j == 4:
                ans += "CD"
            else:
                ans += "C" * j
        elif i == 1:  # Tens place
            if j == 9:
                ans += "XC"
            elif j >= 5:
                ans += "L" + "X" * (j - 5)
            elif j == 4:
                ans += "XL"
            else:
                ans += "X" * j
        else:  # Ones place
            if j == 9:
                ans += "IX"
            elif j >= 5:
                ans += "V" + "I" * (j - 5)
            elif j == 4:
                ans += "IV"
            else:
                ans += "I" * j
    
    return ans

# Example usage:
print(intToRoman(3749))  # Output: "MMMDCCXLIX"








def intToRoman(num: int) -> str:
    thousands = ["", "M", "MM", "MMM"]
    hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
    return thousands[num // 1000] + \
           hundreds[(num % 1000) // 100] + \
           tens[(num % 100) // 10] + \
           ones[num % 10]

# Example usage:
print(intToRoman(3749))  # Output: "MMMDCCXLIX"








def intToRoman(num: int) -> str:
    # List of tuples (value, Roman symbol) sorted from largest to smallest
    val_sym = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    ans = ""
    
    for value, symbol in val_sym:
        count = num // value       # How many times the symbol fits
        ans += symbol * count      # Append that many symbols
        num %= value               # Reduce num for the next iteration
    
    return ans

# Example usage:
print(intToRoman(3749))  # Output: "MMMDCCXLIX"