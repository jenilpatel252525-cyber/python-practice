class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        # remaining '(' in stack are invalid
        remove.update(stack)

        # build result
        return ''.join(
            ch for i, ch in enumerate(s) if i not in remove
        )
