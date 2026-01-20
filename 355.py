s="abcd"

class CombinationIterator:
    def __init__(self,s,k):
        self.s=s
        self.flag=True
        self.k=k
        self.curr=s[:k]
        self.currIdx=[0,1,2]
        self.length=len(s)
        
    def next(self):
        if self.flag:
            self.flag=False
            return self.curr
        ans=[]
        for i in range(1,self.k+1):
            if self.currIdx[-i]<(self.length-i):
                for k in range(self.k-i):
                    ans.append(self.s[self.currIdx[k]])
                for j in range(self.k-i,self.k):
                    self.currIdx[j]=self.currIdx[j-1]+1
                    ans.append(self.s[self.currIdx[j]])
                return "".join(ans)
            
    def hasNext(self):
        if self.currIdx[0]==self.length-self.k:
            return False
        return True
    












class CombinationIterator:
    def __init__(self, s, k):
        self.s = s
        self.k = k
        self.n = len(s)
        self.currIdx = list(range(k))
        self.first = True
        self.done = False

    def next(self):
        # build current combination
        res = "".join(self.s[i] for i in self.currIdx)

        if self.first:
            self.first = False
            return res

        # find index to increment (right to left)
        i = self.k - 1
        while i >= 0 and self.currIdx[i] == self.n - self.k + i:
            i -= 1

        if i < 0:
            self.done = True
            return res

        # increment and reset suffix
        self.currIdx[i] += 1
        for j in range(i + 1, self.k):
            self.currIdx[j] = self.currIdx[j - 1] + 1

        return res

    def hasNext(self):
        return not self.done