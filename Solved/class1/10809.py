#ASCII ord(), chr()
import sys
input = lambda: sys.stdin.readline().rstrip()

alpabet = [-1] * 26

word = input()
for i in range(len(word)):
    location = ord(word[i]) - ord('a')
    if alpabet[location] == -1:
        alpabet[location] = i
result = ' '.join(map(str, alpabet))
print(result)
