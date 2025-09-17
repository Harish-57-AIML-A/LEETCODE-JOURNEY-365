class TwoSum:
    def __init__(self):
        self.table = {}
    
    def add(self, number: int) -> None:
        self.table[number] = self.table.get(number, 0) + 1
    
    def find(self, value: int) -> bool:
        for num in self.table:
            y = value - num
            if y == num:
                if self.table[num] >= 2:
                    return True
            elif y in self.table:
                return True
        return False

# Example Usage
ts = TwoSum()
ts.add(1)
ts.add(3)
ts.add(5)
print(ts.find(4))  # True
print(ts.find(7))  # False

