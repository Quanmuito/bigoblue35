"""
Theo quy tắc về thời trang của đất nước Berland, tất cả nút trên áo đều phải được cài trừ một nút duy nhất không cần phải cài.
Tuy nhiên trong trường hợp đặc biệt với chiếc áo chỉ có đúng một nút thì nút đó phải được cài để áo không bị bay.
Bạn được cho một chiếc áo với N nút. Xác định xem áo đã được cài đúng hay chưa.

Dữ liệu nhập
Dòng đầu tiên chứa một số nguyên N (1 ≤ N ≤ 1000) – số lượng nút trên áo.
Dòng tiếp theo lần lượt chứa N số là đại diện cho nút cài (số 1) hoặc nút không cài (số 0).

Dữ liệu xuất
In ra YES nếu áo được cài đúng quy tắc, ngược lại in ra NO.

Ví dụ

input
3
1 0 0
output
NO

input
3
1 0 1
output
YES

Giải thích ví dụ
Ví dụ 1: Áo gồm 3 nút, trong đó có 2 nút đã cài và 1 nút không cài, thỏa quy tắc nên in YES.

Ví dụ 2: Áo gồm 3 nút, trong đó có 1 nút đã cài và 2 nút không cài, không thỏa quy tắc nên in NO.
"""

#1

nbrOfPins = int(input())
sequence = input().split(' ')

open = sequence.count('0')
correct = (nbrOfPins == 1 and open == 0) or (nbrOfPins > 1 and open == 1)
print('YES' if correct else 'NO')