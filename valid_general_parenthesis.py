class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
    
def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

class Solution:
    def isValid(self, s: str) -> bool:
        stacks = Stack()
        balance = True
        index = 0

        while index < len(s) and balance:
            symbol = s[index]
            if symbol in '([{':
                stacks.push(symbol)
            else:
                if stacks.is_empty():
                    balance = False
                else:
                    top = stacks.pop()
                    if not matches(top, symbol):
                        balance = False

            index = index + 1
        if balance and stacks.is_empty():
            return True
        else: 
            return False