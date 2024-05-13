"""
Bạn được cho hai mảng A và B gồm các số nguyên được sắp xếp theo thứ tự không giảm. 
Kiểm tra xem có thể chọn k số từ mảng A và m số từ mảng B sao cho mọi số được chọn trong mảng đầu tiên nhỏ hơn mọi số được chọn trong mảng thứ hai.

Dữ liệu nhập
Dòng đầu tiên gồm hai số nguyên nA và nB cách nhau bởi khoảng trắng là kích thước của mảng A và B.
Dòng thứ hai gồm hai số nguyên k và m cách nhau bởi khoảng trắng.
Dòng thứ ba gồm nA số cách nhau bởi khoảng trắng — những phần tử trong mảng A.
Dòng thứ tư gồm nB số cách nhau bởi khoảng trắng — những phần tử trong mảng B.

Dữ liệu xuất
In "YES" nếu có thể chọn k số từ mảng A và m số từ mảng B sao cho mọi số được chọn từ mảng A nhỏ hơn mọi số được chọn từ mảng B.
Ngược lại, in "NO".

Ví dụ
input
3 3
2 1
1 2 3
3 4 5
output
YES

input
3 3
3 3
1 2 3
3 4 5
output
NO

input
5 2
3 1
1 1 1 1 1
2 2
output
YES

Giải thích ví dụ
Ví dụ 1: có thể chọn 1 và 2 từ mảng A và 3 từ mảng B (1<3 và 2<3).

Ví dụ 2: cách duy nhất để chọn k phần tử từ mảng đầu tiên và m phần tử từ mảng thứ hai là chọn tất cả phần tử trong hai mảng, khi này mọi số trong mảng A không nhỏ hơn mọi số trong mảng B.

"""

#5

def convert(string): return int(string)

[lenA, lenB] = list(map(convert, input().split(' ')))
[k, m] = list(map(convert, input().split(' ')))

listA = list(map(convert, input().split(' ')))
listB = list(map(convert, input().split(' ')))

listA.sort()
listB.sort()

selectedA = listA[0 : k]
selectedB = listB[(lenB - m) : ]

# Highest of A is smaller than lowest of B
print('YES' if (selectedA[-1] < selectedB[0]) else 'NO')