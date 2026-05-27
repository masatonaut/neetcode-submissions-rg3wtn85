from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.counts = defaultdict(int)
        self.stacks = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.counts[val] += 1
        freq = self.counts[val]
        self.stacks[freq].append(val)
        self.max_freq = max(self.max_freq, freq)

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()
        self.counts[val] -= 1
        if not self.stacks[self.max_freq]:
            self.max_freq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()