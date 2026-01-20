queries = ["bbb","cc"]

words = ["a","aa","aaa","aaaa"]

from bisect import bisect_right

def f(s: str) -> int:
    smallest = min(s)
    return s.count(smallest)

def numSmallerByFrequency(queries, words):
    # First pass: compute frequencies of words
    word_freqs = [f(w) for w in words]
    word_freqs.sort()

    ans = []
    n = len(word_freqs)

    # Process each query
    for q in queries:
        fq = f(q)
        # count how many word_freqs > fq
        cnt = n - bisect_right(word_freqs, fq)
        ans.append(cnt)

    return ans
