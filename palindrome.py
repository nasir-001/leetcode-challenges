class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def addRear(self, item):
        return self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def palchecker(aString):
    chardeque = Deque()

    chars = "`,.;:!@#$%^&*()-_+='/<>[]{()}|~\"?"

    for ch in aString:
        if ch in chars:
            ch = None
        else:
            if ch != " ":
                chardeque.addRear(ch.lower())

    print(chardeque.items)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()

        if first != last:
            stillEqual = False

    return stillEqual
