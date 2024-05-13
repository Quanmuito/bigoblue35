def solve():
    alphabet = [char for char in 'abcdefghijklmnopqrstuvwxyz']
    for char in sentence:
        if char in alphabet:
            alphabet.remove(char)

    return len(alphabet) == 0


N = int(input().strip())
sentence = input().strip().lower()

print('YES' if solve() else 'NO')