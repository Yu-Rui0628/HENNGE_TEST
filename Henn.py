def Cal_sum_of_square(Inputnum, InputA):
    if Inputnum<=0:
        return 0
    if int(InputA[Inputnum - 1]) < 0:
        return Cal_sum_of_square(Inputnum - 1, InputA)
    return int(InputA[Inputnum - 1])**2 + Cal_sum_of_square(Inputnum - 1, InputA)

def Henn_iterator(sum):
    if sum<=0:
        return 0
    Inputnum = int(input())
    print(Cal_sum_of_square(Inputnum,input().split(" ")))
    Henn_iterator(sum-1)

Henn_iterator(int(input()))