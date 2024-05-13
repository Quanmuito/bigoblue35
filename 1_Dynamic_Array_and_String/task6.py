"""
Một đường thẳng trên trục tọa độ có n phân đoạn, phân đoạn thứ i bắt đầu tại vị trí li và kết thúc tại vị trí ri, phân đoạn này đc kí hiệu là [li, ri].
Bạn cho rằng có một phân đoạn bao lấy tất cả các phân đoạn còn lại. Nói cách khác, có một phân đoạn trong các phân đoạn đã cho chứa các phân đoạn khác. Tìm trong tập các phân đoạn được cho, phân đoạn bao lấy các phân đoạn còn lại, và in ra số thứ tự của nó.
Nết không tồn tại phân đoạn thỏa mãn thì in -1.
Một cách chặt chẽ, một phân đoạn [a, b] bao lấy phân đoạn [c, d] nếu thỏa mãn điều kiện a <= c <= d <= b.

Dữ liệu nhập
Dòng đầu tiên chứa một số nguyên n (1 <= n <= 10^5) - số lượng đoạn hiện có.
n dòng tiếp theo, mỗi dòng chứa thông tin của một phân đoạn. Dòng thứ i chứa hai số nguyên li, ri cách bởi khoảng trắng - hai biên của phân đoạn i.
Đảm bảo rằng không tồn tại hai phân đoạn trùng nhau.

Dữ liệu xuất
In ra số thứ tự của đoạn thỏa yêu cầu đề bài. Nếu không có đoạn nào như vậy thì in ra -1.
Các phân đoạn được đánh số thứ tự từ 1 theo thứ tự xuật hiện của input.

Ví dụ

input
3
3 3
4 4
5 5
output
-1

input
6
1 5
2 3
1 10
7 10
7 7
10 10
output
3
"""

#6

def convert(str): return int(str)

def sortByFirstElement(arr): return arr[0]
def sortByLastElement(arr): return arr[1]

totalLines = convert(input())

nbrOfLines = 0
lines = list([])
while (nbrOfLines < totalLines):
    lines.append(list(map(convert, input().split(' '))))
    nbrOfLines += 1

originalLines = lines.copy()

lines.sort(key = sortByFirstElement)
lowestPoint = lines[0][0]

lines.sort(key = sortByLastElement)
highestPoint = lines[-1][1]

linesHasLowestPoint = list([])
for line in lines:
    if (line[0] == lowestPoint): linesHasLowestPoint.append(line)

linesHasBothPoint = list([])
for line in linesHasLowestPoint:
    if (line[1] == highestPoint): linesHasBothPoint.append(line)

if (len(linesHasBothPoint) > 0):
    for i in range(0, len(originalLines)):
        current = originalLines[i]
        if (current[0] == lowestPoint and current[1] == highestPoint): print(i + 1)
else: print(-1)