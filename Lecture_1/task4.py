"""
Vitaly là một cậu học sinh chăm chỉ chưa từng nghỉ một buổi học nào trong năm năm học ở trường đại học. Cậu ta luôn làm bài đúng giờ và qua mọi kỳ thi.
Trong buổi học cuối cùng giảng viên cho Vitaly hai chuỗi s và t. Hai chuỗi có cùng độ dài, gồm các ký tự latin in thường, chuỗi s có thứ tự từ điển nhỏ hơn chuỗi t.
Vitaly muốn biết có một chuỗi nào có thứ tự từ điển lớn hơn chuỗi s và đồng thời có thứ tự từ điển nhỏ hơn chuỗi t hay không. 
Chuỗi này chỉ gồm các ký tự latin in thường và có độ dài bằng với chuỗi s và t.

Hãy giúp Vitaly giải bài tập này nhé!

Chuỗi s = s1s2...sn có thứ tự từ điển nhỏ hơn chuỗi t = t1t2...tn nếu tồn tại giá trị i sao cho s1 = t1, s2 = t2, ... , si-1 = ti -1 , si < ti

Dữ liệu nhập
Dòng đầu tiên chứa chuỗi s (1 <= |s| <= 100) gồm các ký tự tiếng Anh viết thường.
Dòng thứ hai chứa chuỗi t (|t| = |s|) gồm các chữ cái tiếng Anh viết thường.
Chắc chắn rằng chuỗi s và t có cùng độ dài và chuỗi s có thứ tự từ điển nhỏ hơn chuỗi t.

Dữ liệu xuất
Nếu không tồn tại chuỗi thỏa yêu cầu thì in một dòng "No such string" không có nháy kép.

Nếu tồn tại chuỗi thì in ra chuỗi đó. Nếu có nhiều chuỗi thỏa mãn thì có thể in bất kỳ chuỗi nào trong số đó.

Ví dụ
input
k
m
output
l

input
klmnopq
klmpopq
output
klmnopr

input
abcde
abcdf
output
No such string
"""

#4

input1 = input()
input2 = input()

sequence = 'abcdefghijklmnopqrstuvwxyz'

def lastCharUp(str):
    lastCharIndex = sequence.index(str[-1])
    indexUp = (len(sequence) + lastCharIndex + 1) % len(sequence)
    return str[:-1] + sequence[indexUp]

def getString():
    if (input1 == input2): return 'No such string'

    breakpoint = 0
    for i in range(0, len(input1)):
        index1 = sequence.index(input1[i])
        index2 = sequence.index(input2[i])

        if (index1 < index2):
            breakpoint = i
            break

    # Breakpoint at last character => last char go up
    if (breakpoint == len(input1) - 1): output = lastCharUp(input1)
    else:
        nextBreakpoint = breakpoint + 1
        nextBreakpointIndex = sequence.index(input1[nextBreakpoint])

        # If the character next to breakpoint is 'z' => breakpoint to last char go up
        if (nextBreakpointIndex == 25):
            breakpointIndexUp = sequence.index(input1[breakpoint]) + 1
            output = input1[0 : breakpoint] + sequence[breakpointIndexUp]

            restOfInput1 = input1[nextBreakpoint : ]
            for char in restOfInput1:
                index = sequence.index(char)
                indexUp = (len(sequence) + index + 1) % len(sequence)
                output += sequence[indexUp]
        else:
            output = lastCharUp(input1)

    return output if ((output > input1) & (output < input2)) else 'No such string'

print(getString())
