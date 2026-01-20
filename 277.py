from collections import deque

def minMutation(start, end, bank):
    bank = set(bank)
    if end not in bank:
        return -1

    queue = deque([(start, 0)])  # (current_gene, steps)
    visited = set([start])

    while queue:
        gene, steps = queue.popleft()
        if gene == end:
            return steps

        for next_gene in bank:
            if next_gene not in visited:
                # Check if gene and next_gene differ by exactly 1 char
                diff = sum(gene[i] != next_gene[i] for i in range(8))
                if diff == 1:
                    visited.add(next_gene)
                    queue.append((next_gene, steps + 1))
    return -1

# Example
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

print(minMutation(startGene, endGene, bank))  # Output: 2
