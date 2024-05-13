"""
Grigoriy, giống như tên của một anh hùng bộ phim hài nổi tiếng, đã tìm được công việc làm một nhân viên bảo vệ ban đêm tại bảo tàng. 
Vào đêm đầu tiên, anh ta nhận được một chiếc máy dập nổi và phải đi kiểm tra toàn bộ khu trưng bày.
Máy dập nổi là một thiết bị cho phép người dùng in chữ trên cuộn băng keo. Chữ sẽ được in tuần tự, từng chữ một. 
Thiết bị gồm có một vòng quay gồm các ký tự tiếng Anh in thường xếp thành vòng tròn trên đó, một con trỏ đứng yên chỉ vào ký tự hiện tại và một nút bấm để in ký tự được chọn.
Ở mỗi thao tác, vòng quay ký tự có thể quay một bước theo chiều kim đồng hồ hoặc ngược chiều kim đồng hồ.
Ban đầu, con trỏ chỉ vào ký tự 'a'. Những ký tự còn lại được xếp như bên dưới:

abcdefghijklmnopqrstuvwxyz

Sau khi Grigorly thêm một đồ vật mới vào kệ triển lãm, anh ta phải in tên của vật phẩm đó lên miếng băng keo và dán lên. Không bắt buộc phải trả vòng quay về vị trí bắt đầu với con trỏ chỉ vào ký tự 'a'.
Người anh hùng của chúng ta sợ rằng các vật triển lãm sẽ sống dậy và tấn công anh ta, cho nên anh ấy muốn in tên các đồ vật đó nhanh nhất có thể. Hãy giúp Grigoriy với mỗi chuỗi bất kỳ hãy tìm số lần quay ít nhất cần để in chuỗi đó.

Dữ liệu nhập
Một dòng duy nhất chứa tên của vật triển lãm - một chuỗi không rỗng có độ dài không quá 100 ký tự. Chuỗi được cho chỉ có các ký tự tiếng Anh in thường.

Dữ liệu xuất
In số một số nguyên - số lần quay ít nhất để in tên vật triển lãm được cho ở input.

Ví dụ
input
ares
output
34

input
zeus
output
18

input
map
output
35

Giải thích ví dụ

Để in chuỗi từ mẫu đầu tiên, cách tối ưu nhất là thực hiện chuỗi xoay sau:

'a' quay tới 'z': (1 bước ngược chiều kim đồng hồ)
'z' quay tới 'e': (5 bước theo chiều kim đồng hồ)
'e' quay tới 'u': (10 bước ngược chiều kim đồng hồ)
'u' quay tới 's': (2 bước ngược chiều kim đồng hồ)
Vậy để quay được chữ zeus thì bạn cần số bước là: 1+5+10+2=18.
"""

#2

input = input()
sequence = 'abcdefghijklmnopqrstuvwxyz'

output = 0
lastIndex = 0
totalDistance = len(sequence)

for char in input:
    currentIndex = sequence.index(char)
    distance1 = abs(currentIndex - lastIndex)
    distance2 = totalDistance - distance1

    output += distance1 if (distance1 < distance2) else distance2

    lastIndex = currentIndex

print(output)