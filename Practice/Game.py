def end_zeros(num: int) -> int:
     # your code here
     l = list(str(num))
     n = len(l)-1
     s = 0
     try:
        while int(l[n]) == 0:
            s += 1
            n -= 1









if __name__ == '__main__':
     print("Example:")
     print (end_zeros(0))


# def backward_string(val: str) -> str:
#     # your code here
#     s = ''
#     for i in reversed(list(val)):
#         s += i
#     return s
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(backward_string('val'))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert backward_string('val') == 'lav'
    # assert backward_string('') == ''
    # assert backward_string('ohho') == 'ohho'
    # assert backward_string('123456789') == '987654321'
    # print("Coding complete? Click 'Check' to earn cool rewards!")

