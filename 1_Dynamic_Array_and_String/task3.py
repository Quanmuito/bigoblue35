"""
Bear Limak thích xem thể thao trên TV. Anh ta dự định sẽ xem một trận đấu hôm nay. Trận đấu dài 90 phút không có giải lao.
Mỗi phút trận đấu có thể là gay cấn hoặc nhàm chán. Nếu 15 phút liên tục nhàm chán thì Limak sẽ tắt TV ngay lập tức.

Bạn biết rằng có n phút gay cấn tại thời điểm t1, t2, t3,...,tn. Nhiệm vụ của bạn là tính xem Limak sẽ xem bao nhiêu phút của trận đấu.

Dữ liệu nhập
Dòng đầu tiên chứa một số nguyên (1 <= n <= 90) - số lượng đoạn gây cấn.

Dòng tiếp theo gồm n số nguyên t1, t2, t3,...,tn (1 <= t1 <= t2 <= t3 <=...<= tn <= 90) được cho theo thứ tự tăng dần.

Dữ liệu xuất
In số phút Limak xem trận đấu.

Ví dụ
input
3
7 20 88
output
35

input
9
16 20 30 40 50 60 70 80 90
output
15

input
9
15 20 30 40 50 60 70 80 90
output
90

Giải thích ví dụ
Ví dụ 1: phút 21,22,...,35 nhàm chán nên Limak sẽ tắt TV sau phút 35. Do đó, Limak sẽ xem trận đấu đến phút 35

Ví dụ 2: 15 phút đầu tiên nhàm chán

Ví dụ 3: Không có 15 phút liên tục nào nhàm chán nên Limak xem hết cả trận đấu.
"""

#3

def convert(string): return int(string)

nbrOfPeaks = int(input())
peaks = list(map(convert, input().split(' ')))

def getTime():
    last = 0

    for peak in peaks:
        boring = peak - last

        if (boring > 15): return last + 15
        else: last = peak

    output = last + 15
    return output if (output < 90) else 90

print(getTime())