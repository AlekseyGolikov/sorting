"""
    Программа сортирует список по степени близости к 10
"""
class DistanceFrom(object):
    def __init__(self,origin):
        self.origin = origin
    def __call__(self, x):
        return abs(x - self.origin)

nums = [1, 37, 42, 101, 13, 9, -20]
print(nums)
nums.sort(key=DistanceFrom(10))    # Отсортирует по степени близости к числу 10
print(nums)