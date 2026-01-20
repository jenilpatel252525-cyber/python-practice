class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked = None
        self.has_peeked = False

    def peek(self):
        if not self.has_peeked:
            self.peeked = next(self.iterator)
            self.has_peeked = True
        return self.peeked

    def next(self):
        if self.has_peeked:
            result = self.peeked
            self.peeked = None
            self.has_peeked = False
            return result
        return next(self.iterator)

    def hasNext(self):
        return self.has_peeked or self._iterator_has_next()

    def _iterator_has_next(self):
        try:
            # Try peeking one step ahead
            self.peek()
            return True
        except StopIteration:
            return False

nums = iter([1, 2, 3])
it = PeekingIterator(nums)

print(it.peek())    # 1
print(it.next())    # 1
print(it.next())    # 2
print(it.peek())    # 3
print(it.hasNext()) # True
print(it.next())    # 3
print(it.hasNext()) # False