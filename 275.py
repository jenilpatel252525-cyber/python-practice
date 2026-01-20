s = "owoztneoer"

chars=["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]

from collections import Counter

def originalDigits(s: str) -> str:
    # Step 1: Count frequency of each letter
    count = Counter(s)

    # Step 2: Identify digits using unique letters
    out = {}
    out[0] = count['z']  # zero
    out[2] = count['w']  # two
    out[4] = count['u']  # four
    out[6] = count['x']  # six
    out[8] = count['g']  # eight

    # Step 3: Handle overlapping ones
    out[1] = count['o'] - out[0] - out[2] - out[4]   # one
    out[3] = count['h'] - out[8]                     # three
    out[5] = count['f'] - out[4]                     # five
    out[7] = count['s'] - out[6]                     # seven
    out[9] = count['i'] - out[5] - out[6] - out[8]   # nine

    # Step 4: Build result in ascending order
    result = []
    for digit in range(10):
        result.append(str(digit) * out.get(digit, 0))

    return "".join(result)





from collections import Counter

def originalDigits_table(s: str) -> str:
    # Digit words for 0-9
    words = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ]
    
    # Step 1: Build frequency table for each digit word
    digit_freq = [Counter(word) for word in words]
    
    # Step 2: Count frequency of letters in input string
    count = Counter(s)
    
    result = []
    
    # Step 3: Try to subtract digits while possible
    # We go in a special order (to reduce overlaps). Best order is:
    # 0,2,4,6,8 (unique letters), then others
    order = [0,2,4,6,8,1,3,5,7,9]
    
    for digit in order:
        freq = digit_freq[digit]
        # Find how many times this digit can appear
        while all(count[ch] >= freq[ch] for ch in freq):
            # Subtract its letters
            for ch in freq:
                count[ch] -= freq[ch]
            result.append(digit)
    
    # Step 4: Sort and return as string
    result.sort()
    return "".join(map(str, result))
