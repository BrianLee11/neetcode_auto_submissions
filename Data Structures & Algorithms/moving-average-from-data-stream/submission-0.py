from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.window_size = size
        self.deque_max_n = deque(maxlen = self.window_size)

    def next(self, val: int) -> float:
        self.deque_max_n.append(val)
        float_mean = sum(self.deque_max_n) / len(self.deque_max_n)
        return float_mean


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
