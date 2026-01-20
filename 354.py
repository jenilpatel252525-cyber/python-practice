products = ["mobile","mouse","moneypot","monitor","mousepad"]

searchWord = "mouse"

class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        l, r = 0, len(products)

        for i in range(len(searchWord)):
            c = searchWord[i]

            # move left pointer
            while l < r and (len(products[l]) <= i or products[l][i] != c):
                l += 1

            # move right pointer
            while l < r and (len(products[r - 1]) <= i or products[r - 1][i] != c):
                r -= 1

            # take up to 3 results
            res.append(products[l:min(l + 3, r)])

        return res











class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        curr = products[:]   # initially all products
        res = []

        for i, ch in enumerate(searchWord):
            next_curr = []
            for p in curr:
                if len(p) > i and p[i] == ch:
                    next_curr.append(p)
            curr = next_curr
            res.append(curr[:3])

        return res