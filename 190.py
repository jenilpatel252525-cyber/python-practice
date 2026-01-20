def custom_edit_distance(word1, word2):
    # Step 1: Reverse word2
    word2 = word2[::-1]

    # Step 2: Dictionary of char frequency in word2
    freq = {}
    for ch in word2:
        freq[ch] = freq.get(ch, 0) + 1

    word1 = list(word1)
    count = 0
    prev_index = float('inf')

    for ch in word2:
        # Step 3: Find last occurrence of ch before prev_index
        search_end = prev_index if prev_index != float('inf') else len(word1)
        idx = -1
        for i in range(search_end - 1, -1, -1):
            if word1[i] == ch:
                idx = i
                break

        if idx != -1:
            prev_index = idx
            freq[ch] -= 1
        else:
            # Step 4: Try to replace an unneeded char before prev_index
            replaced = False
            for i in range(search_end - 1, -1, -1):
                if freq.get(word1[i], 0) <= 0:
                    word1[i] = ch
                    replaced = True
                    count += 1
                    freq[ch] -= 1
                    prev_index = i
                    break

            # Step 5: If no replacement, insert before prev_index
            if not replaced:
                insert_pos = prev_index if prev_index != float('inf') else len(word1)
                word1.insert(insert_pos, ch)
                count += 1
                freq[ch] -= 1
                prev_index = insert_pos

    return count, "".join(word1)


word1 = "horse"
word2 = "ros"
moves, result = custom_edit_distance(word1, word2)
print("Moves:", moves)
print("Resulting word1:", result)