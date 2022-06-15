"""
    Программа позволяет отслеживать позицию каждого слова в строке s.
    Применяется тип данных defaultdict из модуля collections
"""

from collections import defaultdict

s = 'yeah but no but yeah but no but yeah'
words = s.split()
d = defaultdict(list)
for n, w in enumerate(words):
    d[w].append(n)

print(d)
