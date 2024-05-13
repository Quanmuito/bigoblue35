string = input()

count = 1
for char in string:
    if char.isupper(): count += 1

print(count)