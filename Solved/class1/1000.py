list = input().split()

def add(main):
    result = 0
    for i in range(len(main)):
        result += int(main[i])
    return result
    print(result)

print(add(list))