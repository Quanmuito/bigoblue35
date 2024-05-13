"""
Vanya cố gắng vào trang Codehorses. Anh ấy dùng n mật khẩu riêng biệt cho tất cả trang web, nhưng không nhớ đã dùng cái nào trong lúc đăng ký Codehorses.

Vanya nhập mật khẩu theo thứ tự độ dài không giảm, và nhập mật khẩu có cùng độ dài theo thứ tự tùy ý. Khi Vanya nhập đúng mật khẩu, anh ấy được phép vào trang web. Vanya sẽ không nhập bất kỳ mật khẩu nào hai lần.

Việc nhập mật khẩu bất kỳ sẽ tốn 1 giây. Nếu Vanya nhập sai mật khẩu k lần, thì 5 giây sau anh ta mới có thể thử lần tiếp theo. Tại mỗi thời điểm Vanya có thể nhập mật khẩu, anh ta sẽ thực hiện ngay.

Xác định Vanya cần bao nhiêu giây để vào Codehorses trong trường hợp tốt nhất (tốn ít giây nhất) và trường hợp xấu nhất (tốn nhiều giây nhất).

Dữ liệu nhập
Dòng đầu tiên chứa hai số nguyên n và k (1≤n,k≤100) – số lượng mật khẩu của Vanya và số lần thử thất bại, bị chặn truy cập trang trong 5 giây sau khi thử k lần thất bại. n dòng tiếp theo chứa các mật khẩu, trên mỗi dòng là chuỗi riêng biệt khác rỗng gồm chữ cái và chữ số latin. Mỗi mật khẩu có chiều dài không quá 100.

Dòng cuối chứa mật khẩu Codehorses của Vanya. Đảm bảo mật khẩu Codehorses của Vanya là 1 trong n mật khẩu của anh ta.

Dữ liệu xuất
In 2 số nguyên – thời gian mà Vanya cần để vào được Codehorses trong trường hợp tốt nhất và trường hợp xấu nhất.

Ví dụ
input
5 2
cba
abc
bb1
abC
ABC
abc
output
1 15

input
4 100
11
22
1
2
22
output
3 4

Giải thích ví dụ
Ví dụ 1: Tất cả mật khẩu có chiều dài giống nhau, Vanya có thể nhập mật khẩu đúng vào lần thử đầu tiên cũng như lần cuối. Nếu nhập nó vào lần thử đầu, anh ta tốn 1 giây. Vì vậy trong trường hợp tốt nhất, đáp án là 1.

Mặt khác, nhập nó vào lần thử cuối, nhập 4 mật khẩu khác trước đó. Anh ta tốn 2 giây cho 2 mật khẩu đầu, sau đó đợi 5 giây khi thử sai 2 lần. Sau đó, tốn thêm 2 giây để nhập 2 mật khẩu sai, chờ 5 giây lần nữa, cuối cùng, nhập mật khẩu đúng tốn thêm 1 giây. Tóm lại trường hợp xấu nhất anh ta tốn 15 giây.

Ví dụ 2: Không có cách nào nhập mật khẩu để việc truy cập vào trang bị chặn. Mật khẩu yêu cầu có độ dài 2, Vanya nhập tất cả mật khẩu chiều dài 1, tốn hết 2 giây. Sau đó, trong trường hợp tốt nhất, anh ta nhập mật khẩu đúng ngay thì đáp án cho trường hợp này là 3, nhưng trong trường hợp xấu nhất, anh ta nhập mật khẩu có độ dài 2 sai và sau đó đúng, thì tốn 4 giây.
"""

#7

import math
def convert(string): return int(string)

[n, k] = list(map(convert, input().split(' ')))

nbrOfPasswords = 0
passwords = list([])

while (nbrOfPasswords < n):
    passwords.append(input())
    nbrOfPasswords += 1

correctPassword = input()

def sortByLength(string): return len(string)
passwords.sort(key = sortByLength)

lessChar = 0
equalChar = 0

for password in passwords:
    if (len(password) < len(correctPassword)): lessChar += 1
    if (len(password) == len(correctPassword)): equalChar += 1

# Best case
bestCase = lessChar + 1
bestTimeoutTime = math.ceil(bestCase / k) - 1
bestCaseTime = bestTimeoutTime * 5 + bestCase * 1

worstCase = lessChar + equalChar
worstTimeoutTime = math.ceil(worstCase / k) - 1
worstCaseTime = worstTimeoutTime * 5 + worstCase * 1

print(bestCaseTime, worstCaseTime)